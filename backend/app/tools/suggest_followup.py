from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

def suggest_followup(data: dict):
    prompt = f"""
    You are a CRM assistant for a life sciences company.
    Based on this HCP interaction, suggest 3 specific follow-up actions
    for the sales representative:

    Topics Discussed: {data.get('topics_discussed', '')}
    Outcomes: {data.get('outcomes', '')}
    HCP Sentiment: {data.get('sentiment', 'Neutral')}

    Return exactly 3 follow-up actions as a numbered list.
    Be specific and actionable.
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    return {
        "message": "Follow-up suggestions generated",
        "suggestions": response.content
    }