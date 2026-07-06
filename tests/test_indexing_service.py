from pathlib import Path
from unittest.mock import Mock

from app.schemas.embedding_result import EmbeddingResult
from app.services.indexing_service import IndexingService


def test_index_document_returns_embedding():

    service = IndexingService()

    service.embedding_service.embed = Mock(
        return_value=EmbeddingResult(
            text="chunk",
            embedding=[0.1] * 768
        )
    )

    embeddings = service.index_document(
        Path("tests/resources/sample.pdf")
    )

    assert len(embeddings) > 0


def test_embedding_contains_vector():

    service = IndexingService()

    service.embedding_service.embed = Mock(
        return_value=EmbeddingResult(
            text="chunk",
            embedding=[0.1] * 768
        )
    )

    embeddings = service.index_document(
        Path("tests/resources/sample.pdf")
    )

    assert len(embeddings[0].embedding) == 768