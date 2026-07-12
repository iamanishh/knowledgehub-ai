from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    MODEL_NAME: str = "nomic-embed-text"
    OLLAMA_BASE_URL: str = "http://host.docker.internal:11434"
    LLM_MODEL: str = "llama3.2:3b"

    CHROMA_DIR: str = "./data/chroma"
    UPLOAD_DIR: str = "./uploads"

    TOP_K: int = 3
    SIMILARITY_THRESHOLD: float = 1.0
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()