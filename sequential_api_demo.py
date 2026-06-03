import httpx
import time


def fetch_post(post_id):
    response = httpx.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )

    return response.json()


start = time.time()

for i in range(1, 6):
    result = fetch_post(i)
    print(result["title"])

end = time.time()

print(f"\nExecution Time: {end-start:.2f} seconds")