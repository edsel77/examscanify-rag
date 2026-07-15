from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # APIs
    gemini_api_key: str
    groq_api_key: str

    # Supabase
    supabase_url: str
    supabase_service_role_key: str

    # Upstash Redis
    upstash_redis_rest_url: str
    upstash_redis_rest_token: str

    # LangSmith (set via env, LangChain auto-picks these up)
    langchain_api_key: str = ""
    langchain_tracing_v2: str = "false"
    langchain_project: str = "examscanify-rag"

    # RAG behaviour
    max_retrieval_retries: int = 2
    rate_limit_max_requests: int = 20
    rate_limit_window_hours: int = 1

    # CORS
    cors_origins: str = "https://examscanify.com,http://localhost:3000"

    @property
    def cors_origins_list(self) -> List[str]:
        return [o.strip() for o in self.cors_origins.split(",")]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
