from typing import Any, Dict, List

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from app.config import settings
from app.prompts import rag_prompt
from app.retriever import get_retriever


def format_docs(docs: List[Document]) -> str:
    """
    Format retrieved documents into a clear context block for the LLM.
    """

    formatted_chunks = []

    for index, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown_source")
        content = doc.page_content.strip()

        formatted_chunks.append(
            f"[Document {index} | Source: {source}]\n{content}"
        )

    return "\n\n".join(formatted_chunks)


def extract_sources(docs: List[Document]) -> List[str]:
    """
    Extract unique source filenames from retrieved documents.
    """

    sources = []

    for doc in docs:
        source = doc.metadata.get("source", "unknown_source")
        if source not in sources:
            sources.append(source)

    return sources


def answer_question(question: str) -> Dict[str, Any]:
    """
    Answer a user question using retrieval-augmented generation.
    """

    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    retriever = get_retriever(k=4)

    docs = retriever.invoke(question)

    sources = extract_sources(docs)
    context = format_docs(docs)

    llm = ChatOpenAI(
        model=settings.model_name,
        temperature=0,
    )

    chain = rag_prompt | llm | StrOutputParser()

    answer = chain.invoke(
        {
            "question": question,
            "context": context,
            "sources": ", ".join(sources) if sources else "No sources found",
        }
    )

    return {
        "question": question,
        "answer": answer,
        "sources": sources,
        "retrieved_chunks": len(docs),
    }