# CRM HCP Module — AI-First Log Interaction Screen

## Overview
An AI-powered CRM module for Life Sciences field representatives to log interactions with Healthcare Professionals (HCPs) via a structured form or conversational AI chat.

## Tech Stack
| Layer | Technology |
|---|---|
| Frontend | React.js + Redux Toolkit |
| Backend | Python + FastAPI |
| AI Agent | LangGraph + Groq (gemma2-9b-it) |
| Database | MySQL + SQLAlchemy |
| Font | Google Inter |

## LangGraph Tools
1. **Log Interaction** — Saves interaction + AI summary via Groq LLM
2. **Edit Interaction** — Updates existing logged interaction
3. **Get HCP History** — Fetches all past interactions for an HCP
4. **Suggest Follow-up** — AI generates 3 actionable follow-up steps
5. **Analyze Sentiment** — AI detects HCP sentiment (Positive/Neutral/Negative)

## Project Structure
crm-hcp-module/
├── backend/
│   └── app/
│       ├── agents/     # LangGraph agent
│       ├── tools/      # 5 LangGraph tools
│       ├── models/     # Database models
│       ├── routers/    # FastAPI routes
│       ├── main.py
│       └── database.py
└── frontend/
└── src/
├── components/ # Header, Form, Chat
├── pages/      # LogInteractionPage
├── store/      # Redux store + slice
└── api/        # Axios API calls

## Setup Instructions

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn langgraph langchain-groq langchain-core sqlalchemy pymysql python-dotenv pydantic
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

### Environment Variables
Create `backend/app/.env`:
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost:3306/crm_hcp

## Running the App
- Backend: http://localhost:8000
- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs