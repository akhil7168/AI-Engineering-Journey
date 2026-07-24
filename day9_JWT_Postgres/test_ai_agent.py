from app.services.ai_service import generate_ai_response

questions = [

    "25+75",

    "Calculate (55+45)*10",

    "What is today's date?",

    "Current UTC time",

    "Show CPU usage",

    "Explain JWT Authentication",

    "Explain Redis",

    "How does FastAPI Dependency Injection work?"

]

for question in questions:

    print("=" * 100)

    print(question)

    print("=" * 100)

    response = generate_ai_response(

        session_id="agent",

        prompt=question,

        mode="backend"

    )

    print(response)

    print()