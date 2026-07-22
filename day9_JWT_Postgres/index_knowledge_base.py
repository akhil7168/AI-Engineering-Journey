from app.ai.retriever import load_knowledge_base
from app.ai.vector_store import get_document_count

print("=" * 60)
print("INDEXING KNOWLEDGE BASE")
print("=" * 60)

load_knowledge_base()

print()

print("Documents stored:", get_document_count())