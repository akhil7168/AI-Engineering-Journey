from app.ai.vector_store import (
    collection_exists,
    collection_info,
    get_document_count
)

print("=" * 60)

print("Collection Exists :", collection_exists())

print("Document Count    :", get_document_count())

print(collection_info())

print("=" * 60)