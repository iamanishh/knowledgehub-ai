from fastapi import APIRouter

from app.core.settings import settings
from app.vectorstore.chroma_client import ChromaClient

router = APIRouter(tags=["Health"])

client = ChromaClient()


@router.get(
    "/",
    summary="Health Check",
    description="Returns application health information."
)
def health():

    documents = len(client.get_all()["ids"])

    return {
        "status": "healthy",
        "service": "KnowledgeHub AI",
        "version": "1.0.0",
        "model": settings.MODEL_NAME,
        "documents": documents
    }