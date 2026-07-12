class PromptBuilder:
    """
    Builds the prompt sent to the LLM.
    """

    @staticmethod
    def build(question: str, context: list[str]) -> str:

        joined_context = "\n\n".join(context)

        return f"""
        You are a helpful AI assistant.

        Answer ONLY using the provided context.

        If the answer cannot be found in the context, reply exactly:

        "I don't know based on the provided documents."

        Do not make up information.

        ========================
        CONTEXT
        ========================

        {joined_context}

        ========================
        QUESTION
        ========================

        {question}

        ========================
        ANSWER
        ========================
        """.strip()