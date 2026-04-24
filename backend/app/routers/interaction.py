from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.tools.rag_query_tool import rag_query_tool
from app.database import get_db
from app.tools.log_interaction import log_interaction
from app.tools.edit_interaction import edit_interaction
from app.tools.get_hcp_history import get_hcp_history
from app.tools.suggest_followup import suggest_followup
from app.tools.analyze_sentiment import analyze_sentiment
from langchain_core.messages import HumanMessage
from app.agents.hcp_agent import agent, AgentState
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/interaction", tags=["Interaction"])

# ── Pydantic models ─────────────────────────────────────────
class InteractionCreate(BaseModel):
    hcp_id: int
    interaction_type: str = "Meeting"
    date: str = ""
    time: str = ""
    attendees: str = ""
    topics_discussed: str = ""
    materials_shared: str = ""
    samples_distributed: str = ""
    sentiment: str = "Neutral"
    outcomes: str = ""
    follow_up_actions: str = ""

class InteractionEdit(BaseModel):
    interaction_type: Optional[str] = None
    date: Optional[str] = None
    time: Optional[str] = None
    attendees: Optional[str] = None
    topics_discussed: Optional[str] = None
    materials_shared: Optional[str] = None
    samples_distributed: Optional[str] = None
    sentiment: Optional[str] = None
    outcomes: Optional[str] = None
    follow_up_actions: Optional[str] = None

class ChatMessage(BaseModel):
    message: str
    hcp_id: Optional[int] = None
    interaction_id: Optional[int] = None

class SentimentRequest(BaseModel):
    topics_discussed: str = ""
    outcomes: str = ""
    notes: str = ""

class FollowupRequest(BaseModel):
    topics_discussed: str = ""
    outcomes: str = ""
    sentiment: str = "Neutral"

class RAGQuery(BaseModel):
    query: str
    hcp_id: Optional[int] = None

# ── Tool 1: Log Interaction ─────────────────────────────────
@router.post("/log")
def log(data: InteractionCreate, db: Session = Depends(get_db)):
    return log_interaction(db, data.dict())

# ── Tool 2: Edit Interaction ────────────────────────────────
@router.put("/edit/{interaction_id}")
def edit(interaction_id: int, data: InteractionEdit, db: Session = Depends(get_db)):
    return edit_interaction(db, interaction_id, data.dict(exclude_none=True))

# ── Tool 3: Get HCP History ─────────────────────────────────
@router.get("/history/{hcp_id}")
def history(hcp_id: int, db: Session = Depends(get_db)):
    return get_hcp_history(db, hcp_id)

# ── Tool 4: Suggest Follow-up ───────────────────────────────
@router.post("/suggest-followup")
def followup(data: FollowupRequest):
    return suggest_followup(data.dict())

# ── Tool 5: Analyze Sentiment ───────────────────────────────
@router.post("/analyze-sentiment")
def sentiment(data: SentimentRequest):
    return analyze_sentiment(data.dict())

# ── AI Chat endpoint ────────────────────────────────────────
@router.post("/chat")
def chat(data: ChatMessage, db: Session = Depends(get_db)):
    message_lower = data.message.lower()

    if any(word in message_lower for word in ["log", "save", "record"]):
        return {"response": "Please use the form on the left to log an interaction.", "tool": "log_interaction"}

    elif any(word in message_lower for word in ["history", "previous", "past"]):
        if data.hcp_id:
            return get_hcp_history(db, data.hcp_id)
        return {"response": "Please select an HCP first.", "tool": "get_hcp_history"}

    elif any(word in message_lower for word in ["follow", "next step", "suggest"]):
        return suggest_followup({"topics_discussed": data.message})

    elif any(word in message_lower for word in ["sentiment", "feeling", "mood"]):
        return analyze_sentiment({"topics_discussed": data.message})

    # ✨ RAG routing — for any informational question
    elif any(word in message_lower for word in ["what", "when", "how", "did", "which", "tell me", "who", "where"]):
        return rag_query_tool(db, data.message, data.hcp_id)

    else:
        state = AgentState(
            messages=[HumanMessage(content=data.message)],
            tool_name="",
            tool_input={},
            tool_output=""
        )
        result = agent.invoke(state)
        return {"response": result["tool_output"], "tool": "general_response"}
    
# ── RAG Query endpoint ──────────────────────────────────────
@router.post("/rag-query")
def rag_query(data: RAGQuery, db: Session = Depends(get_db)):
    return rag_query_tool(db, data.query, data.hcp_id)