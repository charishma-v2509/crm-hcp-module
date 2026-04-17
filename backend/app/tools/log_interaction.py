from sqlalchemy.orm import Session
from app.models.interaction import Interaction
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
import json

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

def log_interaction(db: Session, data: dict):
    # Use LLM to summarize the interaction
    prompt = f"""
    You are a CRM assistant for a life sciences company.
    Summarize this HCP interaction in 2-3 sentences:
    
    Topics Discussed: {data.get('topics_discussed', '')}
    Outcomes: {data.get('outcomes', '')}
    Follow-up Actions: {data.get('follow_up_actions', '')}
    
    Return only the summary, nothing else.
    """

    summary_response = llm.invoke([HumanMessage(content=prompt)])
    ai_summary = summary_response.content

    # Save to database
    interaction = Interaction(
        hcp_id=data.get("hcp_id"),
        interaction_type=data.get("interaction_type"),
        date=data.get("date"),
        time=data.get("time"),
        attendees=data.get("attendees"),
        topics_discussed=data.get("topics_discussed"),
        materials_shared=data.get("materials_shared"),
        samples_distributed=data.get("samples_distributed"),
        sentiment=data.get("sentiment"),
        outcomes=data.get("outcomes"),
        follow_up_actions=data.get("follow_up_actions"),
        ai_summary=ai_summary
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return {
        "message": "Interaction logged successfully",
        "interaction_id": interaction.id,
        "ai_summary": ai_summary
    }