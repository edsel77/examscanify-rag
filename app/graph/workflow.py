from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from app.graph.state import GraphState
from app.graph.nodes import (
    retrieve_node,
    grade_documents_node,
    rewrite_query_node,
    generate_node,
    scope_decline_node,
    decide_next_step,
)

# ── Build graph ──────────────────────────────────────────────────────────────
_builder = StateGraph(GraphState)

_builder.add_node("retrieve",        retrieve_node)
_builder.add_node("grade_documents", grade_documents_node)
_builder.add_node("rewrite_query",   rewrite_query_node)
_builder.add_node("generate",        generate_node)
_builder.add_node("scope_decline",   scope_decline_node)

# Entry point
_builder.set_entry_point("retrieve")

# Fixed edges
_builder.add_edge("retrieve",      "grade_documents")
_builder.add_edge("rewrite_query", "retrieve")       # corrective loop
_builder.add_edge("generate",      END)
_builder.add_edge("scope_decline", END)

# Conditional edge after grading
_builder.add_conditional_edges(
    "grade_documents",
    decide_next_step,
    {
        "generate": "generate",
        "rewrite":  "rewrite_query",
        "decline":  "scope_decline",
    },
)

# In-memory checkpointer (enables thread-based state per session_id)
_memory = MemorySaver()

# Compiled graph — import this in the router
graph = _builder.compile(checkpointer=_memory)
