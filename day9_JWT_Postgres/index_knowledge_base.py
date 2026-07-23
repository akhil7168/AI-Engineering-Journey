from app.ai.vector_store import reset_collection
from app.ai.retriever import load_knowledge_base

print("=" * 60)
print("INDEXING KNOWLEDGE BASE")
print("=" * 60)

reset_collection()
load_knowledge_base()

print("\nKnowledge base indexed successfully.")