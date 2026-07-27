from app.agents.tool_registry import ToolRegistry


class PlannerPrompt:

    def __init__(self):
        self.registry = ToolRegistry()

    def build_prompt(self, user_query: str) -> str:

        tool_descriptions = self.registry.get_llm_prompt()

        prompt = f"""
You are an AI Planning Agent.

Your responsibility is to determine which tools are required
to answer the user's request.

Available Tools:

{tool_descriptions}

Instructions:

1. Read the user's request carefully.
2. Select only the tools that are actually needed.
3. If multiple tools are required, include all of them.
4. Extract arguments for each selected tool.
5. Return ONLY valid JSON.
6. Do NOT explain your reasoning.
7. Do NOT return markdown.

JSON Format:

{{
    "tools": [
        {{
            "name": "<tool_name>",
            "arguments": {{
                "<parameter_name>": "<value>"
            }}
        }}
    ]
}}

If no tool is required, return:

{{
    "tools": []
}}

User Request:

{user_query}
"""

        return prompt.strip()