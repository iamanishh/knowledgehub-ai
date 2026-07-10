from unittest.mock import Mock

from fastapi.testclient import TestClient

from app.main import app
from app.api.routes.chat import rag_service

client = TestClient(app)


def test_chat_returns_answer():

    rag_service.answer = Mock(
        return_value="Docker is a container platform."
    )

    response = client.post(
        "/chat",
        json={
            "question": "What is Docker?"
        }
    )

    assert response.status_code == 200

    assert response.json() == {
        "answer": "Docker is a container platform."
    }


def test_chat_requires_question():

    response = client.post(
        "/chat",
        json={}
    )

    assert response.status_code == 422