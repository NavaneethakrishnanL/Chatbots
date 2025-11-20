from memory.vector_store import query_rag

def retrieve_knowledge(query):
    docs = query_rag(query)
    return "\n\n".join(docs)
