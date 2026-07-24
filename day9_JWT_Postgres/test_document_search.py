from app.tools.search_documents import DocumentSearchTool

tool = DocumentSearchTool()

queries = [

    "JWT",

    "Redis",

    "FastAPI",

    "Docker",

    "Dependency Injection"

]

for query in queries:

    print("=" * 100)

    print(query)

    print("=" * 100)

    result = tool.execute(
        query=query
    )

    print(result)

    print()