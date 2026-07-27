from app.agents.tool_registry import ToolRegistry

registry = ToolRegistry()

print()

print("=" * 80)

print("LLM TOOL PROMPT")

print("=" * 80)

print()

print(

    registry.get_llm_prompt()

)