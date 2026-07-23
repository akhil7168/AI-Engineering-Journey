from app.ai.retriever import retrieve_context

questions = [

    "JWT",

    "Redis",

    "FastAPI",

    "Dependency Injection",

    "Database",

    "Machine Learning",

    "Weather",

    "Football"

]

for question in questions:

    print("=" * 80)
    print(question)
    print("=" * 80)

    context = retrieve_context(question)

    if context:
        print(context)
    else:
        print("No relevant context found.")

    print()