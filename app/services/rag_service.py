from ollama import Client
import os

from app.prompts.prompt_builder import PromptBuilder
from app.vectorstore.search_service import SearchService

class RAGService:
    MODEL_NAME = "llama3.2:3b"

    def __init__(self):
        self.search_service = SearchService()

        self.client = Client(
            host=os.getenv(
                "OLLAMA_HOST",
                "http://localhost:11434"
            )
        )

    def answer(self, question: str) -> str:
        context = self.search_service.search(question)
        prompt = PromptBuilder.build(
            question=question,
            context=context
        )
        response = self.client.chat(
            model=self.MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.message.content or ""