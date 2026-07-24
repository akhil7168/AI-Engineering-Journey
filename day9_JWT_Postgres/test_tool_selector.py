from app.agents.tool_selector import ToolSelector

selector = ToolSelector()

queries = [

    "25+36",

    "Calculate 25 * 18",

    "What is today's date?",

    "Current UTC time",

    "Show CPU usage",

    "Explain JWT",

    "Explain Redis",

    "How does FastAPI work?",

    "What is Docker?"

]

for query in queries:

    print("=" * 80)

    print(query)

    print()

    tool = selector.select_tool(query)

    print("Selected Tool:", tool)

    print()