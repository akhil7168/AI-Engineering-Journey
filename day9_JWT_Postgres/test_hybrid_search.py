from app.ai.hybrid_search import hybrid_search

questions = [
    "JWT Authentication",
    "FastAPI",
    "Redis",
    "Database",
    "Dependency Injection"
]

for question in questions:

    print("=" * 80)
    print(question)
    print("=" * 80)

    results = hybrid_search(question)

    for result in results:

        metadata = result["metadata"] or {}

        print(f"Title : {metadata.get('title', 'Unknown')}")
        print(f"Source: {metadata.get('source', 'Unknown')}")
        print(f"Chunk : {metadata.get('chunk', 0)}")

        print(f"Vector Score : {result['vector_score']:.3f}")
        print(f"Keyword Score: {result['keyword_score']}")
        print(f"Final Score  : {result['final_score']:.3f}")

        print("\nContent:")
        print(result["content"][:200])
        print("-" * 80)

    print()