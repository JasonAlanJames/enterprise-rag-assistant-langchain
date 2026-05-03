from pathlib import Path


def test_env_file_is_gitignored():
    gitignore = Path(".gitignore").read_text(encoding="utf-8")
    assert ".env" in gitignore


def test_vectorstore_is_gitignored():
    gitignore = Path(".gitignore").read_text(encoding="utf-8")
    assert "vectorstore/" in gitignore


def test_secrets_are_gitignored():
    gitignore = Path(".gitignore").read_text(encoding="utf-8")
    assert "secrets/" in gitignore


def test_private_key_patterns_are_gitignored():
    gitignore = Path(".gitignore").read_text(encoding="utf-8")
    assert "*.pem" in gitignore
    assert "*.key" in gitignore