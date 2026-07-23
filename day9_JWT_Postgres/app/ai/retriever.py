from app.ai.document_loader import load_text_documents
from app.ai.vector_store import add_documents

from app.ai.hybrid_search import hybrid_search
from app.ai.chunker import chunk_text
from app.ai.context_compressor import compress_context


def load_knowledge_base():
    """
    Load documents, split them into chunks,
    and index them into ChromaDB.
    """

    docs = load_text_documents()

    if not docs:
        print("No documents found.")
        return

    indexed_documents = []

    for doc in docs:

        chunks = chunk_text(doc["content"])

        for index, chunk in enumerate(chunks):

            indexed_documents.append(
                {
                    "id": f"{doc['id']}_{index}",
                    "content": chunk,
                    "metadata": {
                        "title": doc["title"],
                        "source": doc["source"],
                        "chunk": index
                    }
                }
            )

    add_documents(indexed_documents)

    print(f"Indexed {len(indexed_documents)} chunks.")


def retrieve_context(
    question: str,
    top_k: int = 5,
    similarity_threshold: float = 0.40
):

    results = hybrid_search(
        question,
        top_k
    )

    filtered = []

    for result in results:

        if result["final_score"] >= similarity_threshold:

            filtered.append(result)

    if not filtered:
        return ""

    return compress_context(filtered)