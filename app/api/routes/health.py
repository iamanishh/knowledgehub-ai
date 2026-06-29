from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/")
def health():
    return {
        "status": "healthy",
        "service": "KnowledgeHub AI",
        "version": "1.0.0",
    }