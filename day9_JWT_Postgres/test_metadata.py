from app.ai.retriever import retrieve_context

questions = [
    "Explain JWT Authentication",
    "What is Redis?",
    "Explain FastAPI",
    "What is PostgreSQL?"
]

for question in questions:

    print("=" * 80)
    print(question)
    print("=" * 80)

    context = retrieve_context(question)

    print(context)
    print()