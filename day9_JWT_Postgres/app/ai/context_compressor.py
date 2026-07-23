from typing import List


def compress_context(
    results: List[dict],
    max_chunks: int = 3,
    max_characters: int = 2500
):
    """
    Compress retrieved context before sending to the LLM.

    - Removes duplicate chunks
    - Keeps highest-ranked chunks
    - Limits overall prompt size
    """

    seen = set()

    compressed = []

    total_length = 0

    for result in results:

        content = result["content"].strip()

        if content in seen:
            continue

        seen.add(content)

        metadata = result.get("metadata", {})

        block = f"""
Title: {metadata.get('title','Unknown')}
Source: {metadata.get('source','Unknown')}
Chunk: {metadata.get('chunk',0)}

Content:
{content}
"""

        if total_length + len(block) > max_characters:
            break

        compressed.append(block)

        total_length += len(block)

        if len(compressed) >= max_chunks:
            break

    return "\n" + "=" * 60 + "\n".join(compressed)