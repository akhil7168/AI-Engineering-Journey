import asyncio
import httpx
import time


async def fetch_post(post_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        )

        return response.json()


async def main():
    tasks = [
        fetch_post(1),
        fetch_post(2),
        fetch_post(3),
        fetch_post(4),
        fetch_post(5)
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result["title"])


start = time.time()

asyncio.run(main())

end = time.time()

print(f"\nExecution Time: {end-start:.2f} seconds")