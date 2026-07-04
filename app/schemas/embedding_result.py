from pydantic import BaseModel

class EmbeddingResult(BaseModel):
    text: str
    embedding: list[float]
