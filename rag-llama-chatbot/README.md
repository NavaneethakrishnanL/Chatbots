# RAG Llama Chatbot (PDF + URL + Memory)

This is a fully local, privacy-safe Llama chatbot with:

✔ RAG from PDFs  
✔ RAG from URLs  
✔ Conversation memory  
✔ Local embeddings (ChromaDB)  
✔ Local Llama inference (llama.cpp)  
✔ FastAPI backend  

## Run

pip install -r requirements.txt
python app.py

Upload PDFs:
POST /upload_pdf

Add URL:
POST /add_url

Chat:
POST /chat
