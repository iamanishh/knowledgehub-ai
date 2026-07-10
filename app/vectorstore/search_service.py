from app.services.embedding_service import EmbeddingService
from app.vectorstore.chroma_client import ChromaClient

class SearchService:
    """
    Searches ChromaDB for the most relevant chunks
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_db = ChromaClient()

    def search(self, query: str, top_k: int = 3) -> list[str]:
        embedding = self.embedding_service.embed(query)

        results = self.vector_db.collection.query(
            query_embeddings=[embedding.embedding],
            n_results=top_k,
        )

        documents = results["documents"][0]

        return documents


