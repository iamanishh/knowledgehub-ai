from fastapi import FastAPI


from app.api.routes.health import router as health_router
from app.api.routes.documents import router as document_router
from app.exceptions.handlers import register_exception_handlers
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="KnowledgeHub AI",
    version="1.0.0",
    description="Enterprise RAG Knowledge Assistant",
)

register_exception_handlers(app)

app.include_router(health_router)
app.include_router(document_router)
app.include_router(chat_router)

