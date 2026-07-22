from app.services.ai_service import (
    generate_streaming_response
)

print("=" * 60)
print("STREAMING TEST")
print("=" * 60)

for token in generate_streaming_response(
    session_id="stream-test",
    prompt="Explain JWT Authentication",
    mode="backend"
):
    print(token, end="", flush=True)

print("\n\nStreaming completed.")