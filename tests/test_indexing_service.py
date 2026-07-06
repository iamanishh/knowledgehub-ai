from pathlib import Path

from app.services.indexing_service import IndexingService


def test_index_document_returns_embedding():

    service = IndexingService()

    embeddings = service.index_document(
        Path("tests/resources/sample.pdf")
    )

    assert len(embeddings) > 0


def test_embedding_contains_vector():

    service = IndexingService()

    embeddings = service.index_document(
        Path("tests/resources/sample.pdf")
    )
    assert len(embeddings[0].embedding) == 768