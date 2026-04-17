from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from typing import TypedDict, List
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

# ── LLM setup ──────────────────────────────────────────────
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

# ── State: what the agent remembers ────────────────────────
class AgentState(TypedDict):
    messages: List
    tool_name: str
    tool_input: dict
    tool_output: str

# ── Router: decide which tool to call ──────────────────────
def router(state: AgentState):
    last_message = state["messages"][-1].content.lower()

    if "log" in last_message or "save" in last_message or "record" in last_message:
        return "log_interaction"
    elif "edit" in last_message or "update" in last_message or "change" in last_message:
        return "edit_interaction"
    elif "history" in last_message or "previous" in last_message or "past" in last_message:
        return "get_hcp_history"
    elif "follow" in last_message or "next step" in last_message or "suggest" in last_message:
        return "suggest_followup"
    elif "sentiment" in last_message or "feeling" in last_message or "mood" in last_message:
        return "analyze_sentiment"
    else:
        return "general_response"

# ── General response node ───────────────────────────────────
def general_response(state: AgentState):
    response = llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))
    state["tool_output"] = response.content
    return state

# ── Build the graph ─────────────────────────────────────────
def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("general_response", general_response)

    graph.set_conditional_entry_point(
        router,
        {
            "log_interaction": END,
            "edit_interaction": END,
            "get_hcp_history": END,
            "suggest_followup": END,
            "analyze_sentiment": END,
            "general_response": "general_response",
        }
    )

    graph.add_edge("general_response", END)

    return graph.compile()

agent = build_agent()