Enterprise RAG Assistant with LangChain
A production-style Retrieval-Augmented Generation assistant built with LangChain, FastAPI, Chroma, OpenAI embeddings, and LangSmith-ready tracing.
This project demonstrates how to build an enterprise knowledge assistant that answers questions from private documents with source citations and refusal behavior when the answer is not available in the uploaded context.

Author
Built by Jason Alan James  
GitHub: https://github.com/jasonalanjames  
Portfolio: https://jasonajames.com  
LinkedIn: https://linkedin.com/in/jasonalanjames

Portfolio Skill Demonstrated
Enterprise Retrieval-Augmented Generation, also called RAG.

This project shows how to build an AI assistant that retrieves relevant internal knowledge before generating an answer. This is the same core pattern used in many enterprise AI assistants for policies, support knowledge bases, internal documentation, cloud runbooks, security procedures, product docs, and engineering knowledge systems.
Features
LangChain RAG architecture
Document ingestion for `.txt`, `.md`, and `.pdf`
Text chunking
OpenAI embeddings
Chroma vector database
Semantic retrieval
Source-grounded answer generation
Refusal behavior for unsupported questions
FastAPI backend
CLI interface
Dockerized deployment
pytest test coverage
LangSmith tracing support
Secure environment variable handling
Architecture
```text
Documents
   ↓
Document Loaders
   ↓
Text Splitter
   ↓
OpenAI Embeddings
   ↓
Chroma Vector Store
   ↓
Retriever
   ↓
Prompt Template
   ↓
Chat Model
   ↓
Grounded Answer with Sources
```
Tech Stack
Python
LangChain
LangChain OpenAI
LangChain Chroma
ChromaDB
FastAPI
Uvicorn
PyPDF
pytest
Docker
Project Structure
```text
enterprise-rag-assistant-langchain/
├── app/
│   ├── cli.py
│   ├── config.py
│   ├── ingest.py
│   ├── main.py
│   ├── prompts.py
│   ├── rag_chain.py
│   └── retriever.py
├── data/
│   └── sample_docs/
├── evals/
├── tests/
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── pytest.ini
├── README.md
└── requirements.txt
```
Setup
1. Clone the repository
```bash
git clone https://github.com/jasonalanjames/enterprise-rag-assistant-langchain.git
cd enterprise-rag-assistant-langchain
```
2. Create a virtual environment
```bash
python -m venv .venv
```
Windows:
```powershell
.venv\Scripts\activate
```
macOS/Linux:
```bash
source .venv/bin/activate
```
3. Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Create a local environment file
Windows PowerShell:
```powershell
Copy-Item .env.example .env
```
macOS/Linux:
```bash
cp .env.example .env
```
Add your API key to `.env`:
```env
OPENAI_API_KEY=your_real_key_here
```
Do not commit `.env`.
Ingest Documents
```bash
python -m app.ingest
```
This loads documents from:
```text
data/sample_docs/
```
and creates a local vector database at:
```text
vectorstore/
```
Run the CLI
```bash
python -m app.cli
```
Example questions:
```text
Where should API keys be stored?
```
```text
What is the recommended cloud migration approach?
```
```text
What is the CEO's private phone number?
```
For unsupported questions, the assistant should refuse to answer instead of inventing information.
Run the API
```bash
uvicorn app.main:app --reload
```
Open:
```text
http://127.0.0.1:8000/docs
```
Ask a Question Through the API
POST to:
```text
/ask
```
Example request:
```json
{
  "question": "Where should API keys be stored?"
}
```
Expected response should mention environment variables, approved secret management systems, and the security policy sample document.
Rebuild the Vector Store Through the API
POST to:
```text
/ingest
```
This reloads the sample documents, splits them, embeds them, and stores them in Chroma.
Run Tests
```bash
pytest
```
Expected result:
```text
12 passed
```
Docker Usage
```bash
docker compose up --build
```
Then open:
```text
http://127.0.0.1:8000/docs
```
Security Notes
This repository intentionally excludes:
API keys
`.env`
local vector databases
logs
credentials
private customer documents
production secrets
Use `.env.example` to show required variables without exposing secrets.
Files That Should Never Be Committed
```text
.env
.venv/
vectorstore/
.pytest_cache/
__pycache__/
logs/
secrets/
*.pem
*.key
credentials.json
token.json
```
LangSmith Tracing
To enable LangSmith tracing, set:
```env
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_key_here
LANGSMITH_PROJECT=enterprise-rag-assistant-langchain
```
Evaluation Dataset
A simple starter evaluation dataset is included in:
```text
evals/rag_eval_dataset.json
```
It defines example questions, expected answer content, expected sources, and refusal behavior.
What This Project Demonstrates

This project demonstrates the core enterprise AI engineering pattern behind internal knowledge assistants:
secure document ingestion
semantic retrieval
context-grounded generation
refusal behavior
API deployment
testing
observability readiness
safe secret handling
Resume Bullet
Enterprise RAG Assistant | LangChain, Python, Chroma, FastAPI, OpenAI, Docker  

Built a production-style Retrieval-Augmented Generation assistant with document ingestion, vector retrieval, grounded answer generation, source citations, refusal behavior, pytest coverage, Docker deployment, and LangSmith-ready tracing.

License
Copyright (c) 2026 Jason Alan James. All rights reserved.

This repository is provided for portfolio and demonstration purposes only. No permission is granted to copy, modify, distribute, sublicense, or use this code in commercial or production systems without prior written permission from the author.
