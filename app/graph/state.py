from typing import Annotated, List, TypedDict
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class GraphState(TypedDict):
    """State shared across all LangGraph nodes."""
    question: str                                     # current (possibly rewritten) question
    original_question: str                            # user's original question (unchanged)
    messages: Annotated[List[BaseMessage], add_messages]  # Redis-loaded chat history
    documents: List[Document]                         # retrieved docs (filtered after grading)
    generation: str                                   # final answer text
    retries: int                                      # corrective loop counter
    session_id: str                                   # used for Redis key
    is_scope_violation: bool                          # set True if query is off-topic
