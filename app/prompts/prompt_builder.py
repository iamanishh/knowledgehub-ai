class PromptBuilder:
    """
    Builds the prompt sent to the LLM.
    """

    @staticmethod
    def build(question: str, context: list[str]) -> str:

        joined_context = "\n\n".join(context)

        return f"""
You are an AI assistant.

Answer ONLY using the information provided below.

If the answer is not present in the context, reply:

"I don't know based on the provided documents."

Context:
{joined_context}

Question:
{question}

Answer:
""".strip()