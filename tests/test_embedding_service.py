from unittest.mock import Mock

from app.services.embedding_service import EmbeddingService


def test_embedding_returns_vector():

    service = EmbeddingService()

    fake_response = Mock()
    fake_response.embeddings = [[0.1] * 768]

    service.client.embed = Mock(return_value=fake_response)

    result = service.embed("Python is awesome.")

    assert len(result.embedding) == 768


def test_embedding_is_float_vector():

    service = EmbeddingService()

    fake_response = Mock()
    fake_response.embeddings = [[0.5] * 768]

    service.client.embed = Mock(return_value=fake_response)

    result = service.embed("Docker")

    assert isinstance(result.embedding[0], float)