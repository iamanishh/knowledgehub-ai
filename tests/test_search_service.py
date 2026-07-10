from unittest.mock import Mock

from app.vectorstore.search_service import SearchService
from app.schemas.embedding_result import EmbeddingResult


def test_search_returns_documents():

    service = SearchService()
    service.embedding_service.embed = Mock(
        return_value=EmbeddingResult(
            text="question",
            embedding=[0.1]*768
        )
    )

    service.vector_db.collection.query = Mock(
        return_value={
            "documents": [[
                "Docker uses containers. ",
                "FastAPI is lightweight."
            ]]
        }
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

    service.vector_db.collection.query = Mock(
        return_value={
            "documents": [[
                "Docker uses containers."
            ]]
        }
    )

    documents = service.search("Docker")

    assert documents[0] == "Docker uses containers."