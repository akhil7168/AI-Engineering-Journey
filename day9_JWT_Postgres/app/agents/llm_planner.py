import json
import re
from typing import Dict, List

from app.ai.client import chat_with_ai
from app.agents.tool_registry import ToolRegistry
from app.prompts.planner_prompt import PlannerPrompt


class LLMPlanner:

    def __init__(self):

        self.registry = ToolRegistry()

        self.prompt_builder = PlannerPrompt()

    def create_plan(
        self,
        query: str
    ) -> Dict:

        prompt = self.prompt_builder.build_prompt(query)

        messages = [

            {
                "role": "system",
                "content":
                    "You are an expert AI planner. "
                    "Return ONLY valid JSON."
            },

            {
                "role": "user",
                "content": prompt
            }

        ]

        response = chat_with_ai(messages)

        return self.parse_response(response)

    def parse_response(
        self,
        response: str
    ) -> Dict:

        if not response:

            return {

                "tools": []

            }

        response = response.strip()

        response = re.sub(
            r"^```json",
            "",
            response,
            flags=re.IGNORECASE
        )

        response = response.replace(
            "```",
            ""
        ).strip()

        try:

            data = json.loads(response)

        except Exception:

            return {

                "tools": []

            }

        return self.validate_plan(data)

    def validate_plan(
        self,
        plan: Dict
    ) -> Dict:

        validated = []

        for tool in plan.get(
            "tools",
            []
        ):

            name = tool.get("name")

            if not self.registry.tool_exists(name):

                continue

            validated.append({

                "name": name,

                "arguments": tool.get(
                    "arguments",
                    {}
                )

            })

        return {

            "tools": validated

        }

    def list_selected_tools(
        self,
        plan: Dict
    ) -> List[str]:

        return [

            tool["name"]

            for tool in plan.get(
                "tools",
                []
            )

        ]

    def tool_count(
        self,
        plan: Dict
    ) -> int:

        return len(

            plan.get(
                "tools",
                []

            )

        )