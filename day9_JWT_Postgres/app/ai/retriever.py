from app.ai.document_loader import load_text_documents
from app.ai.vector_store import (
    add_documents,
    search_documents
)
from app.ai.chunker import chunk_text

def load_knowledge_base():
    """
    Load documents, split into chunks,
    and index them into ChromaDB.
    """

    docs = load_text_documents()

    if not docs:
        print("No documents found.")
        return

    documents = []
    ids = []
    metadatas = []

    for doc in docs:

        chunks = chunk_text(doc["content"])

        for index, chunk in enumerate(chunks):

            documents.append(chunk)

            ids.append(
                f"{doc['id']}_{index}"
            )

            metadatas.append(
                {
                    "title": doc["title"],
                    "source": doc["source"],
                    "chunk": index
                }
            )

    add_documents(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )

    print(f"Indexed {len(documents)} chunks.")


def retrieve_context(
    question: str,
    top_k: int = 3
):
    """
    Retrieve semantic context along with metadata.
    """

    results = search_documents(
        query=question,
        top_k=top_k
    )

    documents = results.get("documents", [])
    metadatas = results.get("metadatas", [])

    if not documents or not documents[0]:
        return ""

    context_parts = []

    for doc, metadata in zip(
        documents[0],
        metadatas[0]
    ):

        metadata = metadata or {}

        title = metadata.get("title", "Unknown")
        source = metadata.get("source", "Unknown")
        chunk = metadata.get("chunk", 0)

        context_parts.append(
            f"""
Title: {title}
Source: {source}
Chunk: {chunk}

Content:
{doc}
"""
        )

    return "\n" + "=" * 60 + "\n".join(context_parts)