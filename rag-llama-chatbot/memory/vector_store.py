import chromadb
from sentence_transformers import SentenceTransformer

chroma = chromadb.PersistentClient("./memory/chroma")
collection = chroma.get_or_create_collection("rag_memory")

encoder = SentenceTransformer("all-mpnet-base-v2")


def embed(text):
    return encoder.encode(text).tolist()


def add_document(doc_id, chunks):
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            embeddings=[embed(chunk)],
            ids=[f"{doc_id}_{i}"]
        )


def query_rag(query, k=3):
    emb = embed(query)
    result = collection.query(query_embeddings=[emb], n_results=k)
    return result["documents"][0]
