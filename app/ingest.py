from pathlib import Path
from typing import List

from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings


SUPPORTED_EXTENSIONS = {".txt", ".md", ".pdf"}


def load_documents(documents_path: Path) -> List[Document]:
    """Load supported documents from the documents directory."""

    if not documents_path.exists():
        raise FileNotFoundError(f"Documents path does not exist: {documents_path}")

    documents: List[Document] = []

    for file_path in documents_path.rglob("*"):
        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        if file_path.suffix.lower() in {".txt", ".md"}:
            loader = TextLoader(str(file_path), encoding="utf-8")
            loaded_docs = loader.load()
        elif file_path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file_path))
            loaded_docs = loader.load()
        else:
            continue

        for doc in loaded_docs:
            doc.metadata["source"] = file_path.name
            documents.append(doc)

    return documents


def split_documents(documents: List[Document]) -> List[Document]:
    """Split documents into retrieval-friendly chunks."""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""],
    )

    return splitter.split_documents(documents)


def ingest_documents() -> int:
    """Load, split, embed, and persist documents in Chroma."""

    documents = load_documents(settings.documents_path)

    if not documents:
        raise ValueError(f"No supported documents found in {settings.documents_path}")

    chunks = split_documents(documents)

    embeddings = OpenAIEmbeddings(model=settings.embedding_model)

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(settings.vector_db_path),
        collection_name="enterprise_docs",
    )

    return len(chunks)


if __name__ == "__main__":
    count = ingest_documents()
    print(f"Ingested {count} document chunks into {settings.vector_db_path}")