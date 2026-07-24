from app.agents.tool_selector import ToolSelector
from app.agents.tool_registry import execute_tool

selector = ToolSelector()

queries = [

    "45+72",

    "What time is it?",

    "Explain JWT Authentication",

    "CPU usage"

]

for query in queries:

    print("=" * 80)

    print(query)

    tool = selector.select_tool(query)

    print("Selected Tool:", tool)

    if tool == "calculator":

        result = execute_tool(
            tool,
            expression=query.replace("Calculate", "").strip()
        )

    elif tool == "datetime":

        if "utc" in query.lower():
            action = "utc"
        elif "date" in query.lower():
            action = "date"
        elif "day" in query.lower():
            action = "day"
        else:
            action = "time"

        result = execute_tool(
            tool,
            action=action
        )

    elif tool == "document_search":

        result = execute_tool(
            tool,
            query=query
        )

    else:

        result = execute_tool(tool)

    print(result)

    print()