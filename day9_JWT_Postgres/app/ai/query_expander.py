TECHNICAL_EXPANSIONS = {

    "jwt": [
        "JSON Web Token",
        "Authentication",
        "Bearer Token",
        "Security",
        "Authorization"
    ],

    "redis": [
        "Cache",
        "In-Memory Database",
        "Key Value Store",
        "Session Storage"
    ],

    "fastapi": [
        "Python",
        "ASGI",
        "Uvicorn",
        "Dependency Injection",
        "APIRouter"
    ],

    "postgresql": [
        "Database",
        "SQL",
        "Relational Database",
        "Persistence"
    ],

    "docker": [
        "Container",
        "Containerization",
        "Dockerfile",
        "Images",
        "Volumes"
    ],

    "rag": [
        "Retrieval Augmented Generation",
        "Vector Database",
        "Embeddings",
        "Semantic Search"
    ],

    "llm": [
        "Large Language Model",
        "Generative AI",
        "Transformer"
    ]
}


def expand_query(query: str) -> str:
    """
    Expand a user query with related technical terms.
    """

    expanded = [query]

    query_lower = query.lower()

    for keyword, related_terms in TECHNICAL_EXPANSIONS.items():

        if keyword in query_lower:

            expanded.extend(related_terms)

    return " ".join(expanded)