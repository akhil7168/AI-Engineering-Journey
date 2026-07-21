from app.ai.retriever import load_knowledge_base, retrieve_context
from app.services.ai_service import generate_ai_response

SESSION_ID = "rag-test-session"

print("=" * 80)
print("Loading Knowledge Base...")
print("=" * 80)

load_knowledge_base()

questions = [
    "Explain JWT Authentication.",
    "How does FastAPI work?",
    "Where are conversations stored?",
    "What is Redis used for?",
    "What is PostgreSQL?"
]

for question in questions:

    print("\n" + "=" * 80)
    print("QUESTION")
    print("=" * 80)
    print(question)

    print("\nRETRIEVED CONTEXT")
    print("-" * 80)

    context = retrieve_context(question)

    print(context)

    print("\nAI RESPONSE")
    print("-" * 80)

    answer = generate_ai_response(
        session_id=SESSION_ID,
        prompt=question,
        mode="backend"
    )

    print(answer)

print("\n")
print("=" * 80)
print("RAG PIPELINE TEST COMPLETED")
print("=" * 80)