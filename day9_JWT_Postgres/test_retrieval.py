from app.ai.retriever import retrieve_context

questions = [
    "Explain JWT",
    "How does authentication work?",
    "What is Redis?",
    "Tell me about PostgreSQL",
    "Explain FastAPI"
]

for question in questions:

    print("=" * 70)
    print("Question:", question)

    context = retrieve_context(question)

    print("\nRetrieved Context:\n")
    print(context)
    print()