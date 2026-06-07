# Healthcare CRM — AI-Powered HCP Interaction Module

An agentic CRM system for Life Sciences field reps to log, analyze, and act on Healthcare Professional (HCP) interactions — powered by LangGraph, RAG, and Groq LLMs.

## What makes this interesting

Most CRMs are just glorified forms. This one routes user intent through a **LangGraph agent** that selects from 5 specialized tools, generates AI summaries, detects HCP sentiment, and suggests follow-up actions — all in real time via a conversational chat UI or a structured form.

Built end-to-end in 60 hours as a technical assignment.

---

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | React.js + Redux Toolkit |
| Backend | FastAPI (Python) |
| AI Agent | LangGraph + Groq (gemma2-9b-it) |
| Database | MySQL + SQLAlchemy |
| RAG | FAISS + HuggingFace embeddings |

---

## Agent tools (LangGraph)

1. **Log Interaction** — saves interaction with AI-generated summary via Groq
2. **Edit Interaction** — updates existing records
3. **Get HCP History** — retrieves all past interactions for an HCP
4. **Suggest Follow-up** — generates 3 actionable next steps
5. **Analyze Sentiment** — classifies HCP sentiment (Positive / Neutral / Negative)

The agent decides which tool to call based on the user's natural language input — no manual routing needed.

---

## Architecture

```
crm-hcp-module/
├── backend/
│   └── app/
│       ├── agents/       # LangGraph agent definition
│       ├── tools/        # 5 tool implementations
│       ├── models/       # SQLAlchemy DB models
│       ├── routers/      # FastAPI route handlers (9 endpoints)
│       ├── main.py
│       └── database.py
└── frontend/
    └── src/
        ├── components/   # Header, Form, Chat (split-panel UI)
        ├── pages/
        ├── store/        # Redux store + slice
        └── api/          # Axios API calls
```

---

## Local setup

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install fastapi uvicorn langgraph langchain-groq langchain-core sqlalchemy pymysql python-dotenv pydantic faiss-cpu sentence-transformers
uvicorn app.main:app --reload
```

Create `backend/app/.env`:

```
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost:3306/crm_hcp
```

### Frontend

```bash
cd frontend
npm install
npm start
```

| Service | URL |
|---|---|
| Backend | http://localhost:8000 |
| Frontend | http://localhost:3000 |
| API Docs | http://localhost:8000/docs |

---

## Key technical decisions

- **LangGraph over plain LangChain** — gives explicit state management and tool routing without brittle if-else chains
- **FAISS for RAG** — local vector store, no external API needed for embedding retrieval
- **Redux Toolkit** — predictable state for the split-panel UI (form + chat share the same interaction state)
- **SQLAlchemy** — ORM lets us swap DB without rewriting query logic

