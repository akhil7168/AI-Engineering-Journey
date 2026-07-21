from app.ai.embeddings import embed_text

text = "What is JWT Authentication?"

embedding = embed_text(text)

print(f"Embedding Dimension : {len(embedding)}")

print()

print("First 10 values:")

print(embedding[:10])