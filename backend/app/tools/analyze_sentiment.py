from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

def analyze_sentiment(data: dict):
    prompt = f"""
    You are a CRM assistant for a life sciences company.
    Analyze the sentiment of this HCP interaction and return ONE word only:
    Positive, Neutral, or Negative.

    Topics Discussed: {data.get('topics_discussed', '')}
    Outcomes: {data.get('outcomes', '')}
    Notes: {data.get('notes', '')}

    Return only one word: Positive, Neutral, or Negative.
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    sentiment = response.content.strip()

    return {
        "message": "Sentiment analyzed successfully",
        "sentiment": sentiment
    }