from app.ai.retriever import retrieve_context

question = "Explain JWT Authentication"

context = retrieve_context(question)

print("=" * 80)

print("Prompt Size")

print("=" * 80)

print(
    len(context),
    "characters"
)

print()

print(context)