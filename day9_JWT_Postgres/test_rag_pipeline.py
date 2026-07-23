from app.ai.query_expander import expand_query
from app.ai.hybrid_search import hybrid_search
from app.ai.context_compressor import compress_context
from app.services.ai_service import generate_ai_response

SESSION_ID = "evaluation"

questions = [

    "Explain JWT Authentication",

    "What is Redis?",

    "Explain FastAPI Dependency Injection",

    "How does PostgreSQL store data?",

    "What is AI Backend Engineering?"

]

for question in questions:

    print("=" * 100)
    print("QUESTION")
    print("=" * 100)

    print(question)

    expanded = expand_query(question)

    print("\nExpanded Query")
    print("-" * 100)

    print(expanded)

    results = hybrid_search(
        expanded,
        top_k=5
    )

    print("\nRetrieved Chunks")
    print("-" * 100)

    for r in results:

        metadata = r["metadata"] or {}

        print(
            f"{metadata.get('title')} | "
            f"{r['final_score']:.3f}"
        )

    print("\nCompressed Context")
    print("-" * 100)

    print(
        compress_context(results)
    )

    print("\nAI Response")
    print("-" * 100)

    response = generate_ai_response(
        session_id=SESSION_ID,
        prompt=question,
        mode="backend"
    )

    print(response)

    print("\n")