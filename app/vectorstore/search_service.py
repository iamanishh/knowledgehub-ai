from app.services.embedding_service import EmbeddingService
from app.vectorstore.chroma_client import ChromaClient
from app.schemas.search_result import SearchResult
from app.core.logging import logger
from app.core.settings import settings

class SearchService:
    """
    Searches ChromaDB for the most relevant chunks
    """
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_db = ChromaClient()

    def search(self, query: str) -> list[SearchResult]:
        embedding = self.embedding_service.embed(query)

        results = self.vector_db.search(
            embedding.embedding,
            settings.TOP_K
        )

        filtered_results = []

        for result in results:
            if result.distance < settings.SIMILARITY_THRESHOLD:

                logger.info(
                    "Accepted chunk | filename=%s | chunk=%s | distance=%.3f",
                    result.filename,
                    result.chunk,
                    result.distance,
                )

                filtered_results.append(result)

            else:
                logger.info(
                    "Rejected chunk | filename=%s | chunk=%s | distance=%.3f",
                    result.filename,
                    result.chunk,
                    result.distance,
                )

        logger.info(
            "Search complete | query='%s' | retrieved=%d | kept=%d",
            query,
            len(results),
            len(filtered_results),
        )


        return filtered_results


