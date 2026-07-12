from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    # LLM
    MODEL_NAME: str
    OLLAMA_BASE_URL: str
    LLM_MODEL: str


    # Storage
    CHROMA_DIR: str
    UPLOAD_DIR: str

    # RAG
    TOP_K: int = 3
    SIMILARITY_THRESHOLD: float = 1.0
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100

    class Config:
        env_file = ".env"


settings = Settings()

