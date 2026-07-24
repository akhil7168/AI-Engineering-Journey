from app.agents.tool_registry import execute_tool

print("=" * 80)
print("Calculator")
print("=" * 80)

print(

    execute_tool(

        "calculator",

        expression="55*88"

    )

)

print()

print("=" * 80)
print("DateTime")
print("=" * 80)

print(

    execute_tool(

        "datetime",

        action="datetime"

    )

)

print()

print("=" * 80)
print("Document Search")
print("=" * 80)

print(

    execute_tool(

        "document_search",

        query="Redis"

    )

)