from sentence_transformers import SentenceTransformer

# Load a lightweight, fast embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts: list) -> list:
    """
    Convert a list of text strings into vector embeddings.
    Returns a list of numpy arrays.
    """
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings

def embed_query(query: str):
    """
    Convert a single query string into a vector embedding.
    """
    return model.encode([query], convert_to_numpy=True)[0]