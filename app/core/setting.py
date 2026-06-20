from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME: str
    LLM_MODEL: str

    OLLAMA_BASE_URL: str

    CHROMA_DIR: str
    UPLOAD_DIR: str

    class Config:
        env_file = ".env"


settings = Settings()

