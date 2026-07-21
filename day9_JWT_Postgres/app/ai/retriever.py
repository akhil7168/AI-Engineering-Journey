from app.ai.vector_store import search_documents, add_documents

DOCUMENTS = [
    {
        "id": "1",
        "title": "JWT Authentication",
        "content": """
JWT (JSON Web Token) is used for stateless authentication.
It consists of Header, Payload, and Signature.
JWT is commonly used with FastAPI authentication.
"""
    },
    {
        "id": "2",
        "title": "FastAPI",
        "content": """
FastAPI is a modern Python web framework.
It supports asynchronous programming,
dependency injection,
automatic OpenAPI documentation,
and high performance.
"""
    },
    {
        "id": "3",
        "title": "Redis",
        "content": """
Redis is an in-memory key-value database.
It is commonly used for caching,
session storage,
and conversation history.
"""
    },
    {
        "id": "4",
        "title": "PostgreSQL",
        "content": """
PostgreSQL is a relational database.
It stores users,
notes,
AI conversations,
and application data.
"""
    }
]


def load_knowledge_base():
    """
    Load all documents into ChromaDB.
    """

    documents = [doc["content"] for doc in DOCUMENTS]
    ids = [doc["id"] for doc in DOCUMENTS]
    metadatas = [{"title": doc["title"]} for doc in DOCUMENTS]

    add_documents(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )


def retrieve_context(question: str, top_k: int = 3) -> str:
    """
    Retrieve relevant context using semantic search.
    """

    results = search_documents(
        query=question,
        top_k=top_k
    )

    documents = results.get("documents", [])

    if not documents or not documents[0]:
        return ""

    return "\n\n".join(documents[0])