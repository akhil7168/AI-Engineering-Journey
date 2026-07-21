from app.ai.vector_store import (
    add_documents,
    search_documents,
    get_document_count
)

documents = [
    "JWT is used for authentication.",
    "FastAPI is a Python backend framework.",
    "Redis stores cached data.",
    "PostgreSQL is a relational database."
]

ids = [
    "1",
    "2",
    "3",
    "4"
]

print("Adding documents...")

add_documents(
    documents=documents,
    ids=ids
)

print()

print("Documents in DB:", get_document_count())

print()

print("Searching...")

results = search_documents(
    "Explain JWT Authentication"
)

print()

print(results)