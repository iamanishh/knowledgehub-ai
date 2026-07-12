from unittest.mock import Mock

from app.services.rag_service import RAGService
from app.schemas.search_result import SearchResult

def test_rag_returns_answer():

    service = RAGService()

    service.search_service.search = Mock(
        return_value=[
            SearchResult(
                text="Docker is a container platform",
                filename="resume.pdf",
                chunk=0,
                distance=0.2
            )
        ]
    )
    fake_response = Mock()
    fake_response.message.content = "Docker is a container platform"

    service.client.chat = Mock(
        return_value=fake_response
    )
    answer = service.answer(
        "What is Docker?"
    )
    assert answer == "Docker is a container platform"


def test_search_called_once():

    service = RAGService()

    service.search_service.search = Mock(
        return_value=[
            SearchResult(
                text="Context",
                filename="resume.pdf",
                chunk=0,
                distance=0.2
            )
        ]
    )

    fake_response = Mock()
    fake_response.message.content = "Answer"

    service.client.chat = Mock(
        return_value=fake_response
    )

    service.answer("Question")

    service.search_service.search.assert_called_once()