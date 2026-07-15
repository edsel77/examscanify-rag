"""
One-time knowledge base ingestion script.
Run this after setting up your .env to populate Supabase pgvector.

Usage:
    cd /path/to/examscanify-rag
    python scripts/ingest.py
"""

import sys
import os

# Allow imports from project root
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from dotenv import load_dotenv
load_dotenv()

from langchain_core.documents import Document
from langchain_community.vectorstores import SupabaseVectorStore
from supabase import create_client

from app.config import settings
from app.retriever.embedder import embeddings
from app.knowledge.chunks import KNOWLEDGE_CHUNKS


def main():
    print(f"📚 Ingesting {len(KNOWLEDGE_CHUNKS)} knowledge chunks into Supabase pgvector...")

    # Build LangChain Document objects
    docs = [
        Document(
            page_content=chunk["content"],
            metadata=chunk["metadata"],
        )
        for chunk in KNOWLEDGE_CHUNKS
    ]

    # Create Supabase client
    client = create_client(settings.supabase_url, settings.supabase_service_role_key)

    # Clear existing docs to allow re-ingestion
    print("🗑️  Clearing existing examscanify_docs rows...")
    client.table("examscanify_docs").delete().neq("id", "00000000-0000-0000-0000-000000000000").execute()

    # Embed + upsert in batches of 10 (Gemini embedding rate limits)
    batch_size = 10
    total = len(docs)
    for i in range(0, total, batch_size):
        batch = docs[i : i + batch_size]
        print(f"  ↳ Embedding batch {i // batch_size + 1}/{(total + batch_size - 1) // batch_size} "
              f"({len(batch)} chunks)...")
        SupabaseVectorStore.from_documents(
            documents=batch,
            embedding=embeddings,
            client=client,
            table_name="examscanify_docs",
            query_name="match_examscanify_docs",
        )

    print(f"\n✅ Done! {total} chunks embedded and stored in Supabase pgvector.")
    print("   You can now start the FastAPI server: uvicorn main:app --reload")


if __name__ == "__main__":
    main()
