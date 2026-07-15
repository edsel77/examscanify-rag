from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import settings

class TruncatedEmbeddings:
    def __init__(self, base_embeddings, dim):
        self.base_embeddings = base_embeddings
        self.dim = dim
    def embed_documents(self, texts):
        res = self.base_embeddings.embed_documents(texts)
        return [r[:self.dim] for r in res]
    def embed_query(self, text):
        res = self.base_embeddings.embed_query(text)
        return res[:self.dim]

base_embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=settings.gemini_api_key,
)

embeddings = TruncatedEmbeddings(base_embeddings, 768)
