from app.ai.hybrid_search import hybrid_search
from app.ai.context_compressor import compress_context

question = "Explain JWT Authentication"

results = hybrid_search(
    question,
    top_k=10
)

print("=" * 80)
print("Retrieved Chunks")
print("=" * 80)

for r in results:

    print(
        r["metadata"]["title"],
        round(r["final_score"],3)
    )

print()

print("=" * 80)
print("Compressed Context")
print("=" * 80)

print(
    compress_context(results)
)