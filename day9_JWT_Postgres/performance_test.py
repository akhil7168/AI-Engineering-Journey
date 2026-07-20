import time
import requests

BASE_URL = "http://127.0.0.1:8000"

payload = {
    "session_id": "performance_test",
    "prompt": "Explain how JWT authentication works in FastAPI.",
    "mode": "backend"
}

print("=" * 60)
print("NORMAL CHAT PERFORMANCE")
print("=" * 60)

start = time.perf_counter()

response = requests.post(
    f"{BASE_URL}/ai/chat",
    json=payload
)

end = time.perf_counter()

print(f"Status Code : {response.status_code}")
print(f"Total Time  : {(end-start):.3f} sec")

print()

print("=" * 60)
print("STREAMING PERFORMANCE")
print("=" * 60)

start = time.perf_counter()

response = requests.post(
    f"{BASE_URL}/ai/chat/stream",
    json=payload,
    stream=True
)

first_token = None
full_response = ""

for chunk in response.iter_lines():

    if not chunk:
        continue

    decoded = chunk.decode()

    if first_token is None:
        first_token = time.perf_counter()

    full_response += decoded

end = time.perf_counter()

print(f"Status Code        : {response.status_code}")
print(f"Time To First Token: {(first_token-start):.3f} sec")
print(f"Total Time         : {(end-start):.3f} sec")