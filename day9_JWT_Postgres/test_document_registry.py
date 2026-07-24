from app.agents.tool_registry import execute_tool

result = execute_tool(

    "document_search",

    query="Explain JWT Authentication"

)

print(result)

print(

    execute_tool(

        "document_search",

        query=""

    )

)