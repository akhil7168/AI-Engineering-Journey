from app.ai.vector_store import collection

results = collection.get()

print(results.keys())
print()

print("Metadatas:")
print(results["metadatas"])