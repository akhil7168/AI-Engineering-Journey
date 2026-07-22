from app.ai.vector_store import collection

results = collection.get()

print("Documents:", len(results["documents"]))
print("Metadatas:", len(results["metadatas"]))
print("IDs:", len(results["ids"]))