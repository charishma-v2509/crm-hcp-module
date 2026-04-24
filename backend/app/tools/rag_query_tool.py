from sqlalchemy.orm import Session
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from app.rag.retriever import build_index, retrieve_context
from app.rag.chunker import chunk_interactions
from app.rag.embedder import embed_texts
from app.rag.prompt_builder import build_rag_prompt
from app.models.interaction import Interaction
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

def rag_query_tool(db: Session, query: str, hcp_id: int = None):
    from app.models.hcp import HCP

    # Step 1 — Build index
    total = build_index(db, hcp_id=hcp_id)

    if total == 0:
        return {
            "answer": "No interaction data found to answer your question.",
            "source": "rag"
        }

    # Step 2 — Retrieve relevant chunks
    results = retrieve_context(query, top_k=3)

    if not results:
        return {
            "answer": "I could not find relevant information for your query.",
            "source": "rag"
        }

    # Step 3 — Build hcp_map and rechunk with names
    hcps = db.query(HCP).all()
    hcp_map = {h.id: h.name for h in hcps}

    interactions = db.query(Interaction).all()
    chunks = chunk_interactions(interactions, hcp_map=hcp_map)
    chunk_texts = [c["text"] for c in chunks]

    # Match retrieved metadata to chunk texts
    retrieved_texts = []
    for result in results:
        interaction_id = result["metadata"]["interaction_id"]
        for chunk in chunks:
            if chunk["metadata"]["interaction_id"] == interaction_id:
                retrieved_texts.append(chunk["text"])
                break

    # Step 4 — Build prompt
    prompt = build_rag_prompt(query, results, retrieved_texts)

    # Step 5 — LLM response
    response = llm.invoke([HumanMessage(content=prompt)])

    return {
        "answer": response.content,
        "source": "rag",
        "chunks_retrieved": len(results)
    }