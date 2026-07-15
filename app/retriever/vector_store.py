from supabase import create_client
from langchain_community.vectorstores import SupabaseVectorStore
from app.config import settings
from app.retriever.embedder import embeddings

_supabase_client = create_client(
    settings.supabase_url,
    settings.supabase_service_role_key,
)

vector_store = SupabaseVectorStore(
    client=_supabase_client,
    embedding=embeddings,
    table_name="examscanify_docs",
    query_name="match_examscanify_docs",
)

# Standard similarity search (MMR requires SQL RPC to return full embedding vectors)
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5},
)
