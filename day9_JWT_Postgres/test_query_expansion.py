from app.ai.query_expander import expand_query

queries = [

    "JWT",

    "Redis",

    "FastAPI",

    "Docker",

    "PostgreSQL",

    "Explain JWT Authentication"

]

for query in queries:

    print("=" * 70)

    print("Original Query:")
    print(query)

    print()

    print("Expanded Query:")
    print(expand_query(query))

    print()