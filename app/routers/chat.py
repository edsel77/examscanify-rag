import json
import uuid
from datetime import datetime, timedelta
from typing import AsyncGenerator

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from langchain_core.messages import AIMessage, HumanMessage
from pydantic import BaseModel, Field
from sse_starlette.sse import EventSourceResponse

from app.config import settings
from app.graph.workflow import graph
from app.memory.redis_memory import get_session_history, async_redis_client

router = APIRouter()


# ── Request / Response models ─────────────────────────────────────────────────

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()))


# ── Redis Rate Limiter ────────────────────────────────────────────────────────

class RedisRateLimiter:
    def __init__(self, max_req: int, window_hours: int):
        self.max_req = max_req
        self.window_seconds = window_hours * 3600

    async def check(self, ip: str) -> tuple[bool, int, datetime]:
        key = f"examscanify:ratelimit:{ip}"
        
        # Increment the counter
        count = await async_redis_client.incr(key)
        
        # If this is the first request, set the expiration
        if count == 1:
            await async_redis_client.expire(key, self.window_seconds)
            ttl = self.window_seconds
        else:
            ttl = await async_redis_client.ttl(key)
            if ttl == -1: # No expiration was set somehow, fix it
                await async_redis_client.expire(key, self.window_seconds)
                ttl = self.window_seconds
                
        now = datetime.utcnow()
        ttl = ttl if ttl > 0 else self.window_seconds
        reset_at = now + timedelta(seconds=ttl)
        
        if count > self.max_req:
            return False, 0, reset_at
            
        remaining = self.max_req - count
        return True, remaining, reset_at


_limiter = RedisRateLimiter(
    max_req=settings.rate_limit_max_requests,
    window_hours=settings.rate_limit_window_hours,
)


# ── SSE streaming endpoint ────────────────────────────────────────────────────

@router.post("/chat")
async def chat(request: Request, body: ChatRequest):
    # ── CORS headers for SSE response ────────────────────────────────────────
    # EventSourceResponse bypasses FastAPI's CORSMiddleware on streaming
    # responses, so we inject the headers manually here.
    origin = request.headers.get("origin", "*")
    cors_headers = {
        "Access-Control-Allow-Origin": origin,
        "Access-Control-Allow-Credentials": "true",
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no",  # disable Nginx buffering for SSE
    }

    # ── Rate limit ──────────────────────────────────────────────────────────
    client_ip = request.headers.get("x-forwarded-for", request.client.host).split(",")[0].strip()
    allowed, remaining, reset_at = await _limiter.check(client_ip)
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail={
                "error": "Rate limit exceeded",
                "reset_at": reset_at.isoformat(),
                "message": f"You have reached the limit of {settings.rate_limit_max_requests} "
                           f"requests per hour. Please try again after {reset_at.strftime('%H:%M UTC')}.",
            },
        )

    # ── Load Redis conversation history ─────────────────────────────────────
    history = get_session_history(body.session_id)
    past_messages = await history.aget_messages()

    # ── Stream events from LangGraph ─────────────────────────────────────────
    async def event_generator() -> AsyncGenerator[str, None]:
        full_response = ""
        generation_started = False
        scope_violation = False

        try:
            async for event in graph.astream_events(
                {
                    "question":          body.message,
                    "original_question": body.message,
                    "messages":          past_messages,
                    "documents":         [],
                    "generation":        "",
                    "retries":           0,
                    "session_id":        body.session_id,
                    "is_scope_violation": False,
                },
                config={"configurable": {"thread_id": body.session_id}},
                version="v2",
            ):
                kind = event["event"]
                meta = event.get("metadata", {})
                node  = meta.get("langgraph_node", "")
                
                print(f"DEBUG: {kind} | Node: {node}")

                # ── Stream tokens only from the generate node ────────────────
                if kind == "on_chat_model_stream" and node == "generate":
                    generation_started = True
                    chunk = event["data"]["chunk"]
                    token = chunk.content if hasattr(chunk, "content") else ""
                    if token:
                        full_response += token
                        payload = json.dumps({"token": token, "remaining": remaining})
                        yield payload

                # ── Scope decline node finished ──────────────────────────────
                elif kind == "on_chain_end" and node == "scope_decline":
                    scope_violation = True
                    output = event["data"].get("output", {})
                    decline_msg = output.get("generation", "")
                    if decline_msg:
                        full_response = decline_msg
                        payload = json.dumps(
                            {"token": decline_msg, "remaining": remaining, "scope_violation": True}
                        )
                        yield payload

            # ── Persist to Redis ─────────────────────────────────────────────
            if full_response:
                await history.aadd_messages(
                    [
                        HumanMessage(content=body.message),
                        AIMessage(content=full_response),
                    ]
                )

            # ── Done signal ──────────────────────────────────────────────────
            yield json.dumps({'done': True, 'scope_violation': scope_violation, 'remaining': remaining})

        except Exception as exc:
            error_str = str(exc)
            # Groq 413 / token-per-minute rate-limit — give a friendly message
            if "413" in error_str or "rate_limit_exceeded" in error_str or "Request too large" in error_str:
                yield json.dumps({
                    "error": "Your conversation is getting long. Please start a new chat session to continue.",
                    "code": "context_too_long",
                })
            else:
                yield json.dumps({"error": error_str})

    return EventSourceResponse(event_generator(), headers=cors_headers)


# ── Health check ──────────────────────────────────────────────────────────────

@router.get("/health")
async def health():
    return {"status": "ok", "service": "examscanify-rag"}
