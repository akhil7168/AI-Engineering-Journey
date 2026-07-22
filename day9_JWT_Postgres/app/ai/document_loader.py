from pathlib import Path
from typing import List


KNOWLEDGE_BASE_DIR = Path("knowledge_base")


def load_text_documents() -> List[dict]:
    """
    Load all .txt files from the knowledge_base directory.

    Returns:
        [
            {
                "id": "jwt",
                "title": "jwt",
                "content": "...",
                "source": "jwt.txt"
            }
        ]
    """

    documents = []

    if not KNOWLEDGE_BASE_DIR.exists():
        print("Knowledge base folder not found.")
        return documents

    for file in KNOWLEDGE_BASE_DIR.glob("*.txt"):

        try:

            content = file.read_text(
                encoding="utf-8"
            ).strip()

            if not content:
                continue

            documents.append(
                {
                    "id": file.stem,
                    "title": file.stem.replace("_", " ").title(),
                    "content": content,
                    "source": file.name
                }
            )

        except Exception as e:

            print(f"Failed to load {file.name}: {e}")

    return documents