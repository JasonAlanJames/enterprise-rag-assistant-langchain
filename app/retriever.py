from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.config import settings


def get_vectorstore() -> Chroma:
    """
    Connect to the local Chroma vector store.

    The vector store contains embedded document chunks created during ingestion.
    """

    embeddings = OpenAIEmbeddings(model=settings.embedding_model)

    return Chroma(
        collection_name="enterprise_docs",
        embedding_function=embeddings,
        persist_directory=str(settings.vector_db_path),
    )


def get_retriever(k: int = 4):
    """
    Return a retriever that finds the most relevant document chunks.

    k controls how many chunks are returned for each user question.
    """

    vectorstore = get_vectorstore()

    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k},
    )