from app.services.ai_service import generate_ai_response

questions = [

    "Explain JWT",

    "Explain Redis",

    "Explain FastAPI",

    "Explain PostgreSQL"

]

for question in questions:

    print("=" * 80)

    print(question)

    print("=" * 80)

    response = generate_ai_response(
        session_id="quality-test",
        prompt=question,
        mode="backend"
    )

    print(response)

    print()