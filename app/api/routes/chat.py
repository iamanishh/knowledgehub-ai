from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

rag_service = RAGService()

@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = rag_service.answer(
        request.question
    )

    return ChatResponse(answer=answer)