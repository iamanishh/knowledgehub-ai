from fastapi import FastAPI

app = FastAPI(
    title="KnowledgeHub AI",
    version="1.0.0",
    description="Enterprise RAG Knowledge Assistant",
)

@app.get("/",
         tags=["Health"],
         summary="Health Check"
         )
def health():
    return {
        "status": "healthy",
        "service": "KnowledgeHub AI",
        "version": "1.0.0",
    }