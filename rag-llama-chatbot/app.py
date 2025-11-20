from fastapi import FastAPI, UploadFile
from uuid import uuid4

from load_model import llama
from agents.chatbot_agent import chatbot
from agents.rag_retriever import retrieve_knowledge

from loader.pdf_loader import load_pdf
from loader.url_loader import load_url
from loader.chunker import chunk_text

from memory.vector_store import add_document

app = FastAPI()


@app.post("/chat")
async def chat(message: str, session_id: str = None):
    if session_id is None:
        session_id = str(uuid4())

    retrieved = retrieve_knowledge(message)
    history = chatbot.memory.get(session_id)

    prompt = f"""
Retrieved knowledge:
{retrieved}

History:
{history}

User: {message}
AI:
"""

    out = llama(prompt, max_tokens=256)
    answer = out["choices"][0]["text"]

    chatbot.memory.add(session_id, message, answer)

    return {"session_id": session_id, "answer": answer}


@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile):
    text = load_pdf(file.file)
    chunks = chunk_text(text)
    add_document(file.filename, chunks)
    return {"status": "PDF indexed"}


@app.post("/add_url")
async def add_url(url: str):
    text = load_url(url)
    chunks = chunk_text(text)
    add_document(url, chunks)
    return {"status": "URL indexed"}
