from app.agents.tool_registry import list_tools

print("=" * 60)

print("REGISTERED TOOLS")

print("=" * 60)

for tool in list_tools():

    print()

    print(tool["name"])

    print(tool["description"])