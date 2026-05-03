from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.ingest import ingest_documents
from app.rag_chain import answer_question


app = FastAPI(
    title="Enterprise RAG Assistant",
    description=(
        "Production-style LangChain RAG assistant with document ingestion, "
        "vector retrieval, source citations, and refusal behavior."
    ),
    version="1.0.0",
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Enterprise RAG Assistant is running.",
        "interactive_docs": "/docs",
    }


@app.post("/ingest")
def ingest():
    """
    Load sample documents, split them, embed them, and store them in Chroma.
    """

    try:
        chunk_count = ingest_documents()
        return {
            "status": "success",
            "chunks_ingested": chunk_count,
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/ask")
def ask(request: QuestionRequest):
    """
    Ask a question and receive a source-grounded RAG answer.
    """

    try:
        return answer_question(request.question)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))