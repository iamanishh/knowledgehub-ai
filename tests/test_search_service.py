from unittest.mock import Mock

from app.vectorstore.search_service import SearchService
from app.schemas.embedding_result import EmbeddingResult
from app.schemas.search_result import SearchResult


def test_search_returns_documents():

    service = SearchService()
    service.embedding_service.embed = Mock(
        return_value=EmbeddingResult(
            text="question",
            embedding=[0.1]*768
        )
    )

    service.vector_db.search = Mock(
        return_value=[
            SearchResult(
                text="Docker uses containers.",
                filename="resume.pdf",
                chunk=0,
                distance=0.2,
            ),
            SearchResult(
                text="FastAPI is lightweight.",
                filename="resume.pdf",
                chunk=1,
                distance=0.3,
            ),
        ]
    )
    documents = service.search("What is Docker?")
    assert len(documents) == 2


def test_first_document_matches():

    service = SearchService()

    service.embedding_service.embed = Mock(
        return_value=EmbeddingResult(
            text="question",
            embedding=[0.1] * 768
        )
    )

    service.vector_db.search = Mock(
        return_value=[
            SearchResult(
                text="Docker uses containers.",
                filename="resume.pdf",
                chunk=0,
                distance=0.2,
            )
        ]
    )

    results = service.search("Docker")

    assert len(results) == 1
    assert results[0].text == "Docker uses containers."