import os
import chromadb

from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

from app.core.logging_config import logger


# ============================================================
# Configuration
# ============================================================

CHROMA_DB_PATH = "chroma_db"
COLLECTION_NAME = "knowledge_base"

# ============================================================
# Chroma Client
# ============================================================

client = chromadb.PersistentClient(
    path=CHROMA_DB_PATH,
    settings=Settings(anonymized_telemetry=False)
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)

# ============================================================
# Embedding Model
# ============================================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ============================================================
# Collection Helpers
# ============================================================

def collection_exists() -> bool:
    """
    Returns True if the collection exists.
    """
    try:
        client.get_collection(COLLECTION_NAME)
        return True
    except Exception:
        return False


def get_document_count() -> int:
    """
    Returns the number of indexed documents.
    """
    return collection.count()


def reset_collection():
    """
    Deletes and recreates the collection.
    Useful before a complete re-index.
    """
    global collection

    try:
        client.delete_collection(COLLECTION_NAME)
        logger.info("Existing collection deleted.")

    except Exception:
        logger.info("No existing collection found.")

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    logger.info("Fresh collection created.")


def delete_collection():
    """
    Deletes the collection completely.
    """
    try:
        client.delete_collection(COLLECTION_NAME)
        logger.info("Collection deleted.")

    except Exception as e:
        logger.warning(f"Delete failed: {e}")


# ============================================================
# Document Operations
# ============================================================

def add_documents(documents):
    """
    Inserts or updates documents.
    Safe for repeated indexing.
    """

    if not documents:
        logger.warning("No documents supplied.")
        return

    ids = []
    texts = []
    metadatas = []
    embeddings = []

    for doc in documents:

        ids.append(doc["id"])

        texts.append(doc["content"])

        metadatas.append(
            doc.get("metadata", {})
        )

        embeddings.append(
            embedding_model.encode(
                doc["content"]
            ).tolist()
        )

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    logger.info(
        f"Indexed {len(ids)} document chunks."
    )


# ============================================================
# Search
# ============================================================

def search_documents(
    query,
    top_k=5
):
    """
    Performs semantic search.
    Returns documents, metadata and distances.
    """

    query_embedding = embedding_model.encode(
        query
    ).tolist()

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


# ============================================================
# Collection Information
# ============================================================

def collection_info():
    """
    Returns useful information for debugging.
    """

    return {
        "collection_name": COLLECTION_NAME,
        "database_path": CHROMA_DB_PATH,
        "document_count": get_document_count()
    }