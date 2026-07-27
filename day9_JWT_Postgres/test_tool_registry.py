from app.agents.tool_registry import ToolRegistry

registry = ToolRegistry()

print("=" * 70)

print("AVAILABLE TOOLS")

print("=" * 70)

print()

for tool in registry.get_all_tools().values():

    print(tool)

    print()