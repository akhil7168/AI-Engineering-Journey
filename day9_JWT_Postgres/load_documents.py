from app.ai.retriever import load_knowledge_base
from app.ai.vector_store import get_document_count

print("Loading knowledge base...")

load_knowledge_base()

print()

print(f"Documents indexed: {get_document_count()}")