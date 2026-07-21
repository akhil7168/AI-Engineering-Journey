from sentence_transformers import SentenceTransformer
from typing import List

# Load the embedding model once when the application starts
print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded successfully.")


def embed_text(text: str) -> List[float]:
    """
    Generate an embedding vector for a single text.
    """

    embedding = model.encode(
        text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embedding.tolist()


def embed_documents(documents: List[str]) -> List[List[float]]:
    """
    Generate embeddings for multiple documents.
    """

    embeddings = model.encode(
        documents,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings.tolist()