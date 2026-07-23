from typing import List


def rerank_results(
    vector_results: List[dict],
    keyword_results: List[dict],
    top_k: int = 5
):
    """
    Merge vector and keyword search results.

    If the same chunk appears in both searches,
    boost its score.
    """

    merged = {}

    # --------------------------
    # Add vector search results
    # --------------------------

    for result in vector_results:

        key = result["content"]

        merged[key] = {
            "content": result["content"],
            "metadata": result["metadata"],
            "vector_score": result["score"],
            "keyword_score": 0,
            "final_score": result["score"]
        }

    # --------------------------
    # Merge keyword search
    # --------------------------

    for result in keyword_results:

        key = result["content"]

        if key in merged:

            merged[key]["keyword_score"] = result["score"]

            # Boost if found by both searches
            merged[key]["final_score"] += (
                result["score"] * 0.20
            )

        else:

            merged[key] = {
                "content": result["content"],
                "metadata": result["metadata"],
                "vector_score": 0,
                "keyword_score": result["score"],
                "final_score": result["score"] * 0.20
            }

    results = list(
        merged.values()
    )

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return results[:top_k]