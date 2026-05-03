from app.prompts import RAG_SYSTEM_PROMPT


def test_prompt_requires_context_only_answers():
    assert "Use only the provided context" in RAG_SYSTEM_PROMPT


def test_prompt_contains_refusal_behavior():
    assert "I do not have enough information" in RAG_SYSTEM_PROMPT


def test_prompt_prevents_made_up_answers():
    assert "Do not make up" in RAG_SYSTEM_PROMPT


def test_prompt_requires_sources():
    assert "Sources" in RAG_SYSTEM_PROMPT