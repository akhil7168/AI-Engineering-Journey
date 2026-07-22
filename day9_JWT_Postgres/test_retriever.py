from app.ai.retriever import (
    load_knowledge_base,
    retrieve_context
)

print("Loading knowledge base...")

load_knowledge_base()

questions = [
    "Explain JWT Authentication",
    "What is Redis?",
    "Explain FastAPI",
    "What does PostgreSQL store?",
    "What is AI Backend Engineering?"
]

for question in questions:

    print("\n" + "=" * 70)
    print(question)
    print("-" * 70)

    context = retrieve_context(question)

    print(context)