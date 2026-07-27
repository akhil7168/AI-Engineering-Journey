from app.agents.tool_registry import ToolRegistry

registry = ToolRegistry()

print()

print(registry.tool_exists("calculator"))

print(registry.tool_exists("weather"))

print()

print(registry.get_tool("calculator"))

print()

print(registry.list_tool_names())