from ollama import Client
import os

from app.prompts.prompt_builder import PromptBuilder
from app.vectorstore.search_service import SearchService
from app.core.settings import settings

class RAGService:

    def __init__(self):
        self.search_service = SearchService()

        self.client = Client(
            host=settings.OLLAMA_BASE_URL
        )

    def answer(self, question: str) -> str:

        search_results = self.search_service.search(question)

        if not search_results:
            return "I couldn't find any relevant information in the uploaded documents."

        context = []
        for result in search_results:
            context.append(result.text)


        prompt = PromptBuilder.build(
            question=question,
            context=context
        )

        response = self.client.chat(
            model=settings.LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.message.content or ""