from app.agents.tool_executor import ToolExecutor

executor = ToolExecutor()

print("=" * 80)
print("Calculator")
print("=" * 80)

print(

    executor.execute(

        "calculator",

        expression="(55+45)*8"

    )

)

print()

print("=" * 80)
print("DateTime")
print("=" * 80)

print(

    executor.execute(

        "datetime",

        action="datetime"

    )

)

print()

print("=" * 80)
print("Document Search")
print("=" * 80)

print(

    executor.execute(

        "document_search",

        query="Explain JWT Authentication"

    )

)

print()

print("=" * 80)
print("System Info")
print("=" * 80)

print(

    executor.execute(

        "system_info"

    )

)