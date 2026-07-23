from app.ai.document_loader import load_text_documents
from app.ai.chunker import chunk_text
from app.ai.vector_store import search_documents
from app.ai.reranker import rerank_results
from app.ai.query_expander import expand_query

def keyword_search(query: str):
    """
    Simple keyword search over all documents.
    """

    docs = load_text_documents()

    query_words = {
        word.lower()
        for word in query.split()
    }

    matches = []

    for doc in docs:

        chunks = chunk_text(doc["content"])

        for index, chunk in enumerate(chunks):

            score = 0

            lower_chunk = chunk.lower()

            for word in query_words:

                if word in lower_chunk:
                    score += 1

            if score > 0:

                matches.append(
                    {
                        "content": chunk,
                        "metadata": {
                            "title": doc["title"],
                            "source": doc["source"],
                            "chunk": index
                        },
                        "score": score
                    }
                )

    matches.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return matches

def vector_search(
    query: str,
    top_k: int = 5
):
    """
    Wrapper around ChromaDB search.
    """

    results = search_documents(
        query=query,
        top_k=top_k
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    matches = []

    for doc, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):

        similarity = max(
            0,
            1 - distance
        )

        matches.append(
            {
                "content": doc,
                "metadata": metadata,
                "score": similarity
            }
        )

    return matches

def hybrid_search(
    query: str,
    top_k: int = 5
):
    """
    Combine vector search with keyword search.
    """

    expanded_query = expand_query(query)

    vector_results = vector_search(
    expanded_query,
    top_k
    )

    keyword_results = keyword_search(
    expanded_query
    )

    merged = {}

    for result in vector_results:

        merged[result["content"]] = result

    for result in keyword_results:

        if result["content"] not in merged:

            merged[result["content"]] = result

    final_results = list(
        merged.values()
    )

    final_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return rerank_results(
    vector_results,
    keyword_results,
    top_k
    )