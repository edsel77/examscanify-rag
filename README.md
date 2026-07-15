<p align="center">
  <img src="https://examscanify.com/_next/image?url=%2Fexamscanify-1.png&w=640&q=75" height="100" alt="ExamScanify Logo" />
</p>

<h1 align="center">ExamScanify RAG</h1>

<p align="center">
  <strong>Corrective RAG chatbot microservice for the ExamScanify AI support assistant</strong>
</p>

<p align="center">
  <a href="https://examscanify.com">
    <img src="https://img.shields.io/badge/Live_App-examscanify.com-6C63FF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Live App" />
  </a>
  <a href="https://play.google.com/store/apps/details?id=com.driftapps.scanify">
    <img src="https://img.shields.io/badge/Android-Play_Store-3DDC84?style=for-the-badge&logo=google-play&logoColor=white" alt="Google Play" />
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-27AE60?style=for-the-badge" alt="MIT License" />
  </a>
  <img src="https://img.shields.io/badge/PRs-Welcome-6C63FF?style=for-the-badge" alt="PRs Welcome" />
</p>

---

## ✨ Features

- 🤖 **Corrective RAG pipeline** — LangGraph state machine that rewrites bad queries and retries before giving up
- ⚡ **Real-time streaming** — answers stream token-by-token via Server-Sent Events (SSE)
- 🧠 **Conversation memory** — per-session chat history stored in Upstash Redis with 1-hour TTL
- 🌐 **Multilingual** — automatically detects and responds in the same language as the user's question
- 🔒 **IP-based rate limiting** — configurable rolling-window limit via Upstash Redis
- 📉 **Graceful decline** — politely refuses out-of-scope questions instead of hallucinating
- 🔍 **pgvector similarity search** — ~70 curated knowledge chunks stored in Supabase
- 📊 **LangSmith tracing** — optional full observability over every graph run
- ☁️ **Render-ready** — zero-config deployment via `render.yaml`

---

## 🏗️ Tech Stack

| Layer                   | Technology                                                            | Notes                     |
| ----------------------- | --------------------------------------------------------------------- | ------------------------- |
| **API framework**       | [FastAPI](https://fastapi.tiangolo.com/) + Uvicorn                    | Async, with SSE streaming |
| **RAG orchestration**   | [LangGraph](https://langchain-ai.github.io/langgraph/)                | Corrective RAG pattern    |
| **LLM inference**       | [Groq](https://groq.com) — `llama-3.1-8b-instant`                     | Free tier available       |
| **Embeddings**          | [Google Gemini](https://aistudio.google.com) — `gemini-embedding-001` | 768-dim                   |
| **Vector store**        | [Supabase](https://supabase.com) pgvector                             | Free tier available       |
| **Memory & rate limit** | [Upstash Redis](https://upstash.com)                                  | Free tier available       |
| **Observability**       | [LangSmith](https://smith.langchain.com)                              | Optional, free tier       |
| **Deployment**          | [Render](https://render.com)                                          | Via `render.yaml`         |

### 🤖 Corrective RAG Pipeline

The **ExamScanify AI** chatbot is powered by a Corrective Retrieval-Augmented Generation (CRAG) system. Here's how each component fits together:

| Component           | Technology                                                               | Role                                                                 |
| ------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| **RAG Orchestration**| [LangGraph](https://langchain-ai.github.io/langgraph/)                  | State machine that retrieves, grades, and rewrites queries before answering |
| **Embedding Model** | [Google Gemini](https://aistudio.google.com) — `gemini-embedding-001`   | Converts knowledge chunks into 768-dim dense vectors                 |
| **Vector Index**    | [Supabase](https://supabase.com) pgvector                               | Performs similarity search (`match_examscanify_docs` RPC) to retrieve relevant chunks |
| **Primary LLM**     | [Groq](https://groq.com) — `llama-3.1-8b-instant`                       | Generates fast responses and acts as a judge to grade document relevance |
| **Memory**          | [Upstash Redis](https://upstash.com)                                    | Stores short-lived conversation history (1-hour TTL) for multi-turn chats |
| **API Framework**   | [FastAPI](https://fastapi.tiangolo.com/) + Uvicorn                      | Exposes the `/chat` streaming SSE endpoint and handles rate limiting |

---

## 🧠 How It Works

The chatbot uses a **Corrective RAG** pipeline — a LangGraph state machine that verifies retrieved documents before answering:

```
User Question
      │
      ▼
  [retrieve]             ← pgvector similarity search (Supabase)
      │
      ▼
[grade_documents]        ← LLM batch relevance check (Groq)
      │
      ├── relevant    →  [generate]      → stream answer → END
      ├── not relevant (retries left) →  [rewrite_query] → [retrieve] (loop)
      └── not relevant (no retries)  →  [scope_decline]  → polite decline → END
```

If retrieved documents are irrelevant, the graph **rewrites the query** and retries — up to `MAX_RETRIEVAL_RETRIES` times — before gracefully declining.

---

## 🚀 Getting Started

### Prerequisites

- [Python](https://www.python.org/) 3.11+
- Free accounts on: [Google AI Studio](https://aistudio.google.com/app/apikey) · [Groq](https://console.groq.com/keys) · [Supabase](https://supabase.com) · [Upstash](https://upstash.com)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/examscanify-rag.git
cd examscanify-rag
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in all values. Each variable has a comment with a direct link to get that key.

### 5. Set up the Supabase database

1. Create a new project on [supabase.com](https://supabase.com)
2. Go to **SQL Editor** in your Supabase dashboard
3. Paste and run [`sql/schema.sql`](sql/schema.sql)

This creates the `examscanify_docs` table, the HNSW index, and the `match_examscanify_docs` RPC function.

### 6. Ingest the knowledge base

```bash
python scripts/ingest.py
```

Embeds all knowledge chunks using Gemini and upserts them into Supabase pgvector. Runs in batches of 10 to respect embedding rate limits.

> Re-run this any time you update `app/knowledge/chunks.py`.

### 7. Start the development server

```bash
python -m uvicorn main:app --reload --port 8000
```

| Service       | URL                            |
| ------------- | ------------------------------ |
| Chat endpoint | `http://localhost:8000/chat`   |
| Health check  | `http://localhost:8000/health` |
| Swagger docs  | `http://localhost:8000/docs`   |

---

## 📡 API Reference

### `POST /chat`

Streams a RAG response as Server-Sent Events.

**Request body:**

```json
{
  "message": "How does scanning work?",
  "session_id": "optional-uuid-for-conversation-history"
}
```

**SSE event payloads:**

| Payload                                                      | Description                                  |
| ------------------------------------------------------------ | -------------------------------------------- |
| `{"token": "...", "remaining": 18}`                          | Streamed answer token + remaining rate limit |
| `{"token": "...", "scope_violation": true, "remaining": 18}` | Out-of-scope decline message                 |
| `{"done": true, "scope_violation": false, "remaining": 18}`  | Stream complete                              |
| `{"error": "..."}`                                           | Error (e.g. Groq context-too-long)           |

> **Rate limit:** 20 requests per IP per hour by default — configurable via `RATE_LIMIT_MAX_REQUESTS` and `RATE_LIMIT_WINDOW_HOURS` in `.env`.

### `GET /health`

```json
{ "status": "ok", "service": "examscanify-rag" }
```

---

## ☁️ Deployment

This project is configured for **Render** out of the box using a Blueprint.

1. Push your repo to GitHub
2. Create a new **Blueprint Instance** on [render.com](https://render.com) and connect your repo
3. Add all variables from `.env.example` in the Render dashboard
4. Render auto-detects `render.yaml` and deploys

The start command used is:

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## 🗂️ Project Structure

```
examscanify-rag/
├── main.py                      # FastAPI app, CORS, LangSmith setup
├── requirements.txt
├── render.yaml                  # Render deployment config
├── .env.example                 # Copy to .env and fill in your keys
│
├── app/
│   ├── config.py                # Pydantic settings — all config read from .env
│   │
│   ├── graph/
│   │   ├── nodes.py             # LangGraph nodes (retrieve, grade, rewrite, generate, decline)
│   │   ├── state.py             # GraphState TypedDict
│   │   └── workflow.py          # Graph builder + compiled graph
│   │
│   ├── retriever/
│   │   ├── embedder.py          # Gemini embeddings (768-dim)
│   │   └── vector_store.py      # Supabase pgvector retriever
│   │
│   ├── memory/
│   │   └── redis_memory.py      # Upstash Redis session history + async client
│   │
│   ├── routers/
│   │   └── chat.py              # POST /chat (SSE), GET /health, rate limiter
│   │
│   └── knowledge/
│       └── chunks.py            # Curated knowledge base (~70 chunks, 4 categories)
│
├── scripts/
│   └── ingest.py                # One-time script to embed chunks → Supabase
│
└── sql/
    └── schema.sql               # pgvector table + HNSW index + match function
```

---

## 📝 Customising the Knowledge Base

The chatbot's knowledge lives entirely in [`app/knowledge/chunks.py`](app/knowledge/chunks.py). Each chunk is a dictionary:

```python
{
    "content": "Your knowledge text here...",
    "metadata": {"category": "my-category", "title": "Chunk Title"},
}
```

After editing, re-run `python scripts/ingest.py` to update the vector store. The script clears existing rows before re-ingesting, so it's safe to run repeatedly.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a PR or an issue.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'feat: add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [LangChain / LangGraph](https://langchain-ai.github.io/langgraph/) — Corrective RAG graph framework
- [Groq](https://groq.com) — Blazing-fast LLM inference
- [Supabase](https://supabase.com) — Postgres + pgvector made easy
- [Upstash](https://upstash.com) — Serverless Redis for memory and rate limiting
- [FastAPI](https://fastapi.tiangolo.com/) — Lightning-fast Python API framework

---

<p align="center">Built with ❤️ by <a href="https://driftapps.xyz">Drift Apps</a> · <a href="https://examscanify.com">examscanify.com</a></p>
