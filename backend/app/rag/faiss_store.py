import faiss
import numpy as np

class FAISSStore:
    def __init__(self, dimension: int = 384):
        """
        Initialize FAISS index.
        384 is the dimension for all-MiniLM-L6-v2 model.
        """
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []  # stores chunk metadata in same order as index

    def add_chunks(self, embeddings: np.ndarray, metadata_list: list):
        """
        Add embeddings and their metadata to the FAISS index.
        """
        self.index.add(embeddings)
        self.metadata.extend(metadata_list)

    def search(self, query_embedding: np.ndarray, top_k: int = 3):
        """
        Search for top_k most similar chunks to the query.
        Returns list of (distance, metadata) tuples.
        """
        query_embedding = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx < len(self.metadata):
                results.append({
                    "distance": float(dist),
                    "metadata": self.metadata[idx]
                })

        return results

    def total_chunks(self):
        return self.index.ntotal


# Global FAISS store instance
faiss_store = FAISSStore()