import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application configuration loaded from environment variables."""

    app_env: str = os.getenv("APP_ENV", "development")
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

    vector_db_path: Path = Path(os.getenv("VECTOR_DB_PATH", "./vectorstore"))
    documents_path: Path = Path(os.getenv("DOCUMENTS_PATH", "./data/sample_docs"))

    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    langsmith_tracing: str = os.getenv("LANGSMITH_TRACING", "false")
    langsmith_project: str = os.getenv(
        "LANGSMITH_PROJECT",
        "enterprise-rag-assistant-langchain",
    )


settings = Settings()