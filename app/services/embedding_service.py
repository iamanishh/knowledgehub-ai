from ollama import Client
from app.schemas.embedding_result import EmbeddingResult
from app.core.settings import settings
import os


class EmbeddingService:
    """
    Generate embedding using ollama
    """
    def __init__(self):
        self.client = Client(
            host=settings.OLLAMA_BASE_URL
        )

    def embed(self, text: str) -> EmbeddingResult:

        response = self.client.embed(
            model=settings.MODEL_NAME,
            input=text
        )

        return EmbeddingResult(
            text=text,
            embedding=response.embeddings[0]
        )