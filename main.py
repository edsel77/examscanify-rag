import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers.chat import router

# ── LangSmith tracing (auto-enabled via env vars) ─────────────────────────────
os.environ.setdefault("LANGCHAIN_TRACING_V2",  settings.langchain_tracing_v2)
os.environ.setdefault("LANGCHAIN_API_KEY",      settings.langchain_api_key)
os.environ.setdefault("LANGCHAIN_PROJECT",      settings.langchain_project)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 ExamScanify RAG service starting...")
    yield
    print("🛑 ExamScanify RAG service shutting down.")


app = FastAPI(
    title="ExamScanify RAG API",
    description="Corrective RAG chatbot for ExamScanify landing page",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(router)
