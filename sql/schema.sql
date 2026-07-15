-- ============================================================
-- ExamScanify RAG — Supabase pgvector Schema
-- Run this in: Supabase Dashboard > SQL Editor
-- ============================================================

-- Step 1: Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Step 2: Knowledge base documents table
-- Note: Gemini text-embedding-004 produces 768-dimensional vectors
CREATE TABLE IF NOT EXISTS examscanify_docs (
  id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  content     TEXT        NOT NULL,
  metadata    JSONB       DEFAULT '{}',
  embedding   VECTOR(768),
  category    TEXT,
  created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- Step 3: HNSW index for fast approximate nearest neighbor search
CREATE INDEX IF NOT EXISTS examscanify_docs_embedding_idx
  ON examscanify_docs
  USING hnsw (embedding vector_cosine_ops)
  WITH (m = 16, ef_construction = 64);

-- Step 4: match_documents function required by LangChain SupabaseVectorStore
CREATE OR REPLACE FUNCTION match_examscanify_docs(
  query_embedding  VECTOR(768),
  match_count      INT     DEFAULT 5,
  filter           JSONB   DEFAULT '{}'
)
RETURNS TABLE (
  id          UUID,
  content     TEXT,
  metadata    JSONB,
  similarity  FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    d.id,
    d.content,
    d.metadata,
    1 - (d.embedding <=> query_embedding) AS similarity
  FROM examscanify_docs d
  WHERE d.metadata @> filter
  ORDER BY d.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;
