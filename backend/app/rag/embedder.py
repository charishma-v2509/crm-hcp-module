from sentence_transformers import SentenceTransformer

# Lazy load — model only loads when first used, not at startup
_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def embed_texts(texts: list) -> list:
    """
    Convert a list of text strings into vector embeddings.
    Returns a list of numpy arrays.
    """
    embeddings = get_model().encode(texts, convert_to_numpy=True)
    return embeddings

def embed_query(query: str):
    """
    Convert a single query string into a vector embedding.
    """
    return get_model().encode([query], convert_to_numpy=True)[0]