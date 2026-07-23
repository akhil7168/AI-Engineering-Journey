from app.ai.hybrid_search import hybrid_search

questions = [

    "JWT",

    "Redis",

    "FastAPI",

    "Dependency Injection",

    "PostgreSQL"

]

for question in questions:

    print("=" * 80)
    print(question)
    print("=" * 80)

    results = hybrid_search(question)

    for result in results:

        metadata = result["metadata"]

        print()

        print(
            metadata.get("title")
        )

        print(
            "Vector Score :",
            round(result["vector_score"], 3)
        )

        print(
            "Keyword Score:",
            result["keyword_score"]
        )

        print(
            "Final Score  :",
            round(result["final_score"], 3)
        )

        print(
            result["content"][:150]
        )

    print()