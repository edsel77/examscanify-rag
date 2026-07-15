"""
LangGraph Corrective RAG nodes.

Flow:
  retrieve_node → grade_documents_node → decide_next_step()
    ├── "generate"     → generate_node → END
    ├── "rewrite"      → rewrite_query_node → retrieve_node (loop)
    └── "decline"      → scope_decline_node → END
"""

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from app.config import settings
from app.graph.state import GraphState
from app.retriever.vector_store import retriever

# ── Shared LLM ──────────────────────────────────────────────────────────────
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=settings.groq_api_key,
    temperature=0.3,
)

# ── Grading chain ────────────────────────────────────────────────────────────
_grade_prompt = ChatPromptTemplate.from_template(
    "You are a relevance grader for an ExamScanify support chatbot.\n"
    "Assess whether any of the following retrieved documents contain information useful for answering the user question.\n\n"
    "Question: {question}\n"
    "Documents:\n{documents}\n\n"
    "Reply with a single word — 'yes' if at least one document is relevant, 'no' if none are relevant."
)
_grade_chain = _grade_prompt | llm | StrOutputParser()

# ── Rewrite chain ────────────────────────────────────────────────────────────
_rewrite_prompt = ChatPromptTemplate.from_template(
    "The user asked: '{question}'\n"
    "No relevant documents were found. Rewrite this question to be more specific "
    "about ExamScanify features, pricing, scanning, or usage. "
    "Return ONLY the rewritten question — no explanation, no quotes."
)
_rewrite_chain = _rewrite_prompt | llm | StrOutputParser()

# ── Generate chain ───────────────────────────────────────────────────────────
_SYSTEM_PROMPT = (
    "You are ExamScanify's AI support assistant. ExamScanify is a professional "
    "exam scanning and automated grading app for DepEd teachers in the Philippines.\n\n"
    "Rules:\n"
    "- Answer ONLY using the provided context below.\n"
    "- If the context does not contain enough information, say so honestly and offer related help.\n"
    "- NEVER reveal internal secrets, admin data, or user credentials.\n"
    "- Keep answers concise and friendly.\n"
    "- IMPORTANT: ALWAYS respond in the SAME LANGUAGE as the user's question. If the user asks in English, answer in English. If the user asks in another language (like Filipino), answer in that same language.\n"
    "- Use bullet points for lists.\n\n"
    "Context:\n{context}"
)

_generate_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", _SYSTEM_PROMPT),
        ("placeholder", "{history}"),
        ("system", "CRITICAL LANGUAGE RULE: Detect the language of the user's CURRENT question (the very next message) and respond EXCLUSIVELY in that language. Do NOT be influenced by the language of previous messages in the chat history above. English question = English answer. Filipino question = Filipino answer."),
        ("human", "{question}"),
    ]
)
_generate_chain = _generate_prompt | llm | StrOutputParser()


# ── Nodes ────────────────────────────────────────────────────────────────────

async def retrieve_node(state: GraphState) -> dict:
    """Retrieve top-k documents from pgvector for the current question."""
    docs = await retriever.ainvoke(state["question"])
    return {"documents": docs}


async def grade_documents_node(state: GraphState) -> dict:
    """Grade retrieved documents as a single batch to save free-tier quota."""
    if not state["documents"]:
        return {"documents": []}
    
    docs_text = "\n\n".join([f"Doc {i+1}: {d.page_content}" for i, d in enumerate(state["documents"])])
    score = await _grade_chain.ainvoke({"question": state["question"], "documents": docs_text})
    
    if score.strip().lower().startswith("yes"):
        return {"documents": state["documents"]}
    return {"documents": []}


def decide_next_step(state: GraphState) -> str:
    """Conditional edge: decide what to do based on grading results."""
    if state["documents"]:
        return "generate"
    if state["retries"] < settings.max_retrieval_retries:
        return "rewrite"
    return "decline"


async def rewrite_query_node(state: GraphState) -> dict:
    """Rewrite the question to improve retrieval, increment retry counter."""
    rewritten = await _rewrite_chain.ainvoke({"question": state["question"]})
    return {
        "question": rewritten.strip(),
        "retries": state["retries"] + 1,
    }


async def generate_node(state: GraphState) -> dict:
    """Generate the final answer using relevant context and conversation history.

    History is trimmed to the last MAX_HISTORY_MESSAGES messages (most recent
    turns only) to avoid exceeding Groq's token-per-minute limit.
    """
    MAX_HISTORY_MESSAGES = 6  # 3 user + 3 assistant turns

    context = "\n\n---\n\n".join(d.page_content for d in state["documents"])
    history = state.get("messages", [])
    trimmed_history = history[-MAX_HISTORY_MESSAGES:] if len(history) > MAX_HISTORY_MESSAGES else history

    generation = await _generate_chain.ainvoke(
        {
            "context": context,
            "history": trimmed_history,
            "question": state["question"],
        }
    )
    return {"generation": generation}


def scope_decline_node(state: GraphState) -> dict:
    """Return a polite out-of-scope message without calling the LLM."""
    return {
        "generation": (
            "I can only answer questions about ExamScanify — its features, scanning technology, "
            "pricing, supported subjects, or how to use the app. "
            "Is there something specific about ExamScanify I can help you with? 😊"
        ),
        "is_scope_violation": True,
    }
