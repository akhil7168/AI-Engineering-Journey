from app.ai.chunker import chunk_text

sample = """
FastAPI is a modern Python web framework.

It supports asynchronous programming.

Dependency Injection.

OpenAPI documentation.

JWT Authentication.

Redis.

PostgreSQL.

Docker.

Artificial Intelligence.

Machine Learning.

Large Language Models.

Vector Databases.

ChromaDB.

Sentence Transformers.

Retrieval-Augmented Generation.
""" * 8

chunks = chunk_text(sample)

print("Total Chunks:", len(chunks))

print()

for i, chunk in enumerate(chunks):

    print("=" * 60)
    print("Chunk", i + 1)
    print("=" * 60)

    print(chunk)

    print()