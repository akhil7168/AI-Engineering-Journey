from app.services.ai_service import build_rag_prompt

questions = [
    "Explain JWT Authentication",
    "What is Redis?",
    "How does FastAPI work?"
]

for question in questions:

    print("=" * 80)
    print(question)
    print("=" * 80)

    print(build_rag_prompt(question))
    print()