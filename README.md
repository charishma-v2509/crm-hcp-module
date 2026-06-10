# 🏥 AI-First Healthcare CRM — HCP Interaction Module

An AI-powered CRM for Life Sciences field representatives to log, analyze, and manage interactions with Healthcare Professionals (HCPs) — built with LangGraph agents, RAG pipeline, FastAPI, and React.

---

## 🔍 Problem It Solves

Pharmaceutical field reps manually log dozens of HCP interactions per week — a time-consuming, error-prone process. This module replaces that with:
- A **structured form** for fast data entry
- A **conversational AI chat** to log interactions in plain English
- **Automated AI summaries, sentiment detection, and follow-up suggestions** generated on every interaction

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 AI Chat Interface | Log interactions conversationally via an LLM-powered assistant |
| 📋 Structured Form | Full-form interaction logging with HCP selection, topics, materials, outcomes |
| 🧠 AI Summary | Auto-generated interaction summary using Groq LLM |
| 💬 Sentiment Detection | AI detects HCP sentiment (Positive / Neutral / Negative) |
| 📌 Follow-up Suggestions | 3 actionable follow-up steps generated per interaction |
| 📜 Interaction History | Fetch and review all past interactions with any HCP |
| ⚡ Agentic Workflow | LangGraph orchestrates all AI tasks as structured tool calls |

---

## 🖼️ Screenshots

### Empty Form + AI Chat Panel
![Empty Form](screenshots/crm-empty.png)

### Logged Interaction with AI Summary & Follow-ups
![Filled Form with AI Output](screenshots/crm-filled.png)

---

## 🏗️ Architecture

```
User (Form / Chat)
       │
       ▼
  React Frontend (Redux Toolkit)
       │  Axios API calls
       ▼
  FastAPI Backend
       │
       ▼
  LangGraph Agent ──── Groq LLM (gemma2-9b-it)
       │
  ┌────┴────────────────────────────┐
  │  Tool 1: Log Interaction        │
  │  Tool 2: Edit Interaction       │
  │  Tool 3: Get HCP History        │
  │  Tool 4: Suggest Follow-up      │
  │  Tool 5: Analyze Sentiment      │
  └────┬────────────────────────────┘
       │
       ▼
  MySQL Database (SQLAlchemy ORM)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React.js, Redux Toolkit, Axios |
| Backend | Python, FastAPI, SQLAlchemy |
| AI Agent | LangGraph, LangChain, Groq API |
| LLM | gemma2-9b-it via Groq |
| Database | MySQL |
| Deployment | Vercel (frontend) |

---

## 🤖 LangGraph Agent — 5 Tools

The core AI engine is a **LangGraph-based agentic workflow** that decides which tool to invoke based on user intent:

1. **`log_interaction`** — Saves structured interaction data + generates AI summary via Groq LLM
2. **`edit_interaction`** — Updates an existing logged interaction by ID
3. **`get_hcp_history`** — Retrieves all past interactions for a specific HCP
4. **`suggest_followup`** — Generates 3 contextual, actionable follow-up recommendations
5. **`analyze_sentiment`** — Detects HCP sentiment from interaction notes (Positive / Neutral / Negative)

---

## 📁 Project Structure

```
crm-hcp-module/
├── backend/
│   └── app/
│       ├── agents/         # LangGraph agent definition
│       ├── tools/          # 5 LangGraph tool implementations
│       ├── models/         # SQLAlchemy database models
│       ├── routers/        # FastAPI route handlers
│       ├── main.py         # App entry point
│       └── database.py     # DB connection setup
└── frontend/
    └── src/
        ├── components/     # Header, InteractionForm, ChatPanel
        ├── pages/          # LogInteractionPage
        ├── store/          # Redux store + interactionSlice
        └── api/            # Axios API service layer
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.9+
- Node.js 16+
- MySQL running locally
- Groq API key (free at [console.groq.com](https://console.groq.com))

### 1. Clone the Repository
```bash
git clone https://github.com/charishma-v2509/crm-hcp-module.git
cd crm-hcp-module
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install fastapi uvicorn langgraph langchain-groq langchain-core sqlalchemy pymysql python-dotenv pydantic
```

Create `backend/app/.env`:
```
GROQ_API_KEY=your_groq_api_key_here
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost:3306/crm_hcp
```

Start the backend:
```bash
uvicorn app.main:app --reload
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm start
```

### 4. Running URLs
| Service | URL |
|---|---|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| API Docs (Swagger) | http://localhost:8000/docs |

---

## 🚀 Live Demo

🔗 **[View Live App](https://crm-hcp-module-seven.vercel.app)**

---

## 💡 What Makes This Different from a CRUD App

Most student CRM projects are basic Create-Read-Update-Delete applications. This project is different:

- **Agentic AI layer** — LangGraph decides which tool to call based on natural language input, not hardcoded logic
- **Dual interaction modes** — users can log via form OR by chatting with the AI assistant
- **LLM-generated intelligence** — every logged interaction automatically gets a summary, sentiment label, and 3 follow-up action items
- **Production-grade structure** — separated routers, models, agents, and tools; not a single-file backend

---

## 👩‍💻 Author

**Varkuti Sai Charishma**
- GitHub: [@charishma-v2509](https://github.com/charishma-v2509)
- LinkedIn: [sai-charishma-varkuti](https://www.linkedin.com/in/sai-charishma-varkuti/)
