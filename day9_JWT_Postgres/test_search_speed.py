import time

from app.ai.hybrid_search import hybrid_search

questions = [

    "JWT",

    "Redis",

    "FastAPI",

    "Docker",

    "Python"

]

times = []

for question in questions:

    start = time.time()

    hybrid_search(question)

    end = time.time()

    elapsed = end - start

    times.append(elapsed)

    print(f"{question}: {elapsed:.4f} sec")

print()

print(
    "Average:",
    round(sum(times) / len(times), 4),
    "seconds"
)