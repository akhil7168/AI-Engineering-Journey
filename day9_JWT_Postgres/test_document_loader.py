from app.ai.document_loader import load_text_documents

documents = load_text_documents()

print(f"Loaded {len(documents)} documents.\n")

for document in documents:

    print("=" * 60)
    print("ID:", document["id"])
    print("Title:", document["title"])
    print("Source:", document["source"])

    print("\nContent:\n")

    print(document["content"])

    print()