from typing import List


def chunk_text(
    text: str,
    chunk_size: int = 400,
    overlap: int = 50
) -> List[str]:
    """
    Split text into overlapping chunks.

    Args:
        text: Input document
        chunk_size: Maximum characters per chunk
        overlap: Number of overlapping characters

    Returns:
        List of text chunks
    """

    text = text.strip()

    if not text:
        return []

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        if end >= len(text):
            break

        start = end - overlap

    return chunks