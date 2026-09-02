import chromadb

def get_chroma_client():
    client = chromadb.PersistentClient(
        path="data/vector_db"
    )

    return client

def get_or_create_collection(client):
    collection = client.get_or_create_collection(
        name = "enterprise_documents"
    )

    return collection

def prepare_chroma_data(chunks: list[dict]):
    ids = []
    documents = []
    metadatas = []
    for chunk in chunks:
        ids.append(chunk["metadata"]["chunk_id"])
        documents.append(chunk["content"])
        metadatas.append(chunk["metadata"])

    return ids, documents, metadatas

def add_chunks_to_collection(
        collection,
        ids,
        documents,
        metadatas,
        embeddings
):
    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )

def search_collection(
        collection,
        query_embedding,
        top_k=3
):
    results = collection.query(
        query_embeddings = [query_embedding], n_results = top_k
    )
    return results