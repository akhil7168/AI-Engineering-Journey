from app.ai.retriever import (
    load_knowledge_base,
    retrieve_context
)

print("Loading knowledge base...")

load_knowledge_base()

print()

queries = [
    "Explain JWT",
    "How does authentication work?",
    "Python backend framework",
    "Where are conversations stored?",
    "What is Redis?"
]

for query in queries:

    print("=" * 60)
    print("Question:", query)
    print()

    context = retrieve_context(query)

    print(context)
    print()