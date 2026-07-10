from unittest.mock import Mock

from app.services.rag_service import RAGService


def test_rag_returns_answer():

    service = RAGService()

    service.search_service.search = Mock(
        return_value=[
            "Docker is a container platform"
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
        return_value=["Context"]
    )

    fake_response = Mock()
    fake_response.message.content = "Answer"

    service.client.chat = Mock(
        return_value=fake_response
    )

    service.answer("Question")

    service.search_service.search.assert_called_once()