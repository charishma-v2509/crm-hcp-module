import numpy as np
from app.rag.chunker import chunk_interactions
from app.rag.embedder import embed_texts, embed_query
from app.rag.faiss_store import faiss_store
from app.models.interaction import Interaction
from sqlalchemy.orm import Session

from app.models.hcp import HCP

def build_index(db: Session, hcp_id: int = None):
    """
    Load interactions from MySQL, chunk them,
    embed them, and store in FAISS index.
    """
    query = db.query(Interaction)
    if hcp_id:
        query = query.filter(Interaction.hcp_id == hcp_id)

    interactions = query.all()

    if not interactions:
        return 0

    # Build hcp_id → name map
    hcps = db.query(HCP).all()
    hcp_map = {h.id: h.name for h in hcps}

    chunks = chunk_interactions(interactions, hcp_map=hcp_map)
    texts = [chunk["text"] for chunk in chunks]
    metadata_list = [chunk["metadata"] for chunk in chunks]

    embeddings = embed_texts(texts).astype("float32")

    faiss_store.index.reset()
    faiss_store.metadata = []
    faiss_store.add_chunks(embeddings, metadata_list)

    return len(chunks)

def retrieve_context(query: str, top_k: int = 3, hcp_id: int = None):
    query_emb = embed_query(query).astype("float32")
    results = faiss_store.search(query_emb, top_k=top_k)
    return results