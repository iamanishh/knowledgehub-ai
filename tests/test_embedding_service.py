from app.services.embedding_service import EmbeddingService

def test_embedding_returns_vector():

    service = EmbeddingService()

    result = service.embed("Python is awesome.")

    assert result.text == "Python is awesome."
    assert len(result.embedding) > 0


def test_embedding_is_float_vector():

    service = EmbeddingService()
    result = service.embed("Docker")

    assert isinstance(result.embedding[0], float)
