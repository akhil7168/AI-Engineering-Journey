import chromadb
from typing import List

from app.ai.embeddings import embed_text

# Persistent Chroma database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="knowledge_base"
)


def add_documents(
    documents: List[str],
    ids: List[str],
    metadatas: List[dict] | None = None
):
    """
    Add documents to the vector database.
    """

    embeddings = [
        embed_text(doc)
        for doc in documents
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search_documents(
    query: str,
    top_k: int = 3
):
    """
    Perform semantic search.
    """

    query_embedding = embed_text(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    return results

def get_document_count():
    """
    Returns number of indexed documents.
    """
    return collection.count()