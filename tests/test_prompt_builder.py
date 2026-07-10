from app.prompts.prompt_builder import PromptBuilder

def test_prompt_contains_question():

    prompt = PromptBuilder.build(
        question="What is Docker?",
        context=["Docker is a container platform"]
    )
    assert "What is Docker?" in prompt


def test_prompt_contains_context():

    prompt = PromptBuilder.build(
        question="Docker?",
        context=["Docker is a awesome"]
    )
    assert "Docker is a awesome" in prompt

def test_prompt_contains_instructions():
    prompt = PromptBuilder.build(
        question="Docker?",
        context=["Docker."]
    )
    assert "Answer ONLY using the information" in prompt