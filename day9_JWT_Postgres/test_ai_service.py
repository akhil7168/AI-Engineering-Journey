from app.services.ai_service import generate_ai_response

session_id = "test-session"

questions = [
    "Explain JWT Authentication",
    "What is Redis?",
    "Tell me about PostgreSQL",
    "What is FastAPI?"
]

for question in questions:

    print("=" * 70)
    print("Question:")
    print(question)

    print("\nAnswer:\n")

    answer = generate_ai_response(
        session_id=session_id,
        prompt=question,
        mode="general"
    )

    print(answer)
    print()