from upstash_redis import Redis
from upstash_redis.asyncio import Redis as AsyncRedis
from langchain_community.chat_message_histories import UpstashRedisChatMessageHistory
from app.config import settings

_redis_client = Redis(
    url=settings.upstash_redis_rest_url,
    token=settings.upstash_redis_rest_token,
)

async_redis_client = AsyncRedis(
    url=settings.upstash_redis_rest_url,
    token=settings.upstash_redis_rest_token,
)


def get_session_history(session_id: str) -> UpstashRedisChatMessageHistory:
    """Return a Redis-backed message history for the given session.
    Each session expires after 1 hour of inactivity (TTL in seconds).
    """
    return UpstashRedisChatMessageHistory(
        session_id=f"examscanify:chat:{session_id}",
        url=settings.upstash_redis_rest_url,
        token=settings.upstash_redis_rest_token,
        ttl=3600,
    )
