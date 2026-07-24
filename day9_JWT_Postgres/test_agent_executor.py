from app.agents.tool_selector import ToolSelector
from app.agents.tool_executor import ToolExecutor

selector = ToolSelector()
executor = ToolExecutor()

queries = [

    "55+88",

    "What is today's date?",

    "Current UTC time",

    "Show CPU usage",

    "Explain JWT Authentication"

]

for query in queries:

    print("=" * 100)

    print("Query:", query)

    tool = selector.select_tool(query)

    print("Selected Tool:", tool)

    if tool == "calculator":

        result = executor.execute(

            tool,

            expression=query.replace("Calculate", "").strip()

        )

    elif tool == "datetime":

        lower = query.lower()

        if "utc" in lower:
            action = "utc"
        elif "date" in lower:
            action = "date"
        elif "day" in lower:
            action = "day"
        else:
            action = "time"

        result = executor.execute(

            tool,

            action=action

        )

    elif tool == "document_search":

        result = executor.execute(

            tool,

            query=query

        )

    else:

        result = executor.execute(

            tool

        )

    print(result)
    print()