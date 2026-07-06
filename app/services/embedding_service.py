from ollama import Client
from app.schemas.embedding_result import EmbeddingResult
import os


class EmbeddingService:
    """
    Generate embedding using ollama
    """

    MODEL_NAME = "nomic-embed-text"

    def __init__(self):
        self.client = Client(
            host=os.getenv("OLLAMA_HOST", "http://localhost:11434")
        )

    def embed(self, text: str) -> EmbeddingResult:

        response = self.client.embed(
            model=self.MODEL_NAME,
            input=text
        )

        return EmbeddingResult(
            text=text,
            embedding=response.embeddings[0]
        )