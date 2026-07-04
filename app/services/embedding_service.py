import ollama
from app.schemas.embedding_result import EmbeddingResult

class EmbeddingService:
    """
    Generate embedding using ollama
    """

    MODEL_NAME = "nomic-embed-text"

    def embed(self, text: str) -> EmbeddingResult:

        response = ollama.embed(
            model=self.MODEL_NAME,
            input=text
        )
        return EmbeddingResult(
            text=text,
            embedding=response.embeddings[0]
        )