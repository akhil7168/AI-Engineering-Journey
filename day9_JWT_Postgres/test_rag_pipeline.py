from app.ai.retriever import (
    load_knowledge_base,
    retrieve_context
)

from app.services.ai_service import (
    generate_ai_response
)

SESSION_ID = "day37-rag-test"

print("=" * 80)
print("LOADING KNOWLEDGE BASE")
print("=" * 80)

load_knowledge_base()

questions = [
    "Explain JWT Authentication",
    "What is Redis?",
    "Explain FastAPI Dependency Injection",
    "What does PostgreSQL store?",
    "What is AI Backend Engineering?"
]

for question in questions:

    print("\n" + "=" * 80)
    print("QUESTION")
    print("=" * 80)
    print(question)

    print("\nRETRIEVED CONTEXT")
    print("-" * 80)

    context = retrieve_context(question)

    print(context)

    print("\nAI RESPONSE")
    print("-" * 80)

    response = generate_ai_response(
        session_id=SESSION_ID,
        prompt=question,
        mode="backend"
    )

    print(response)

print("\n")
print("=" * 80)
print("RAG PIPELINE TEST COMPLETED")
print("=" * 80)