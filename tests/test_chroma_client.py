import uuid

from app.schemas.embedding_result import EmbeddingResult
from app.vectorstore.chroma_client import ChromaClient


def test_add_embedding():

    client = ChromaClient()

    embedding = EmbeddingResult(
        text="FastAPI",
        embedding=[0.1]*768
    )

    client.add(
        document_id=str(uuid.uuid4()),
        embedding=embedding,
        metadata={
            "filename": "sample.pdf"
        }
    )

    assert client.collection.count() > 0