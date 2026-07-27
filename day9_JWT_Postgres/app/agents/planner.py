import json
import re
import time

from app.ai.client import chat_with_ai
from app.agents.agent_state import AgentState
from app.agents.tool_registry import ToolRegistry
from app.agents.tool_validator import ToolValidator
from app.agents.planner_metadata import PlannerMetadata
from app.agents.planner_logger import PlannerLogger
from app.prompts.planner_prompt import PlannerPrompt


class Planner:
    """
    Hybrid Planner

    1. Rule-Based Planning
    2. LLM Planning
    3. Tool Validation
    4. Planner Metadata
    """

    def __init__(self):

        self.calculator_pattern = re.compile(
            r'^[\d\+\-\*\/\(\)\s\.]+$'
        )

        self.registry = ToolRegistry()
        self.prompt_builder = PlannerPrompt()
        self.validator = ToolValidator()
        self.logger = PlannerLogger()

    # =====================================================
    # Rule Planner
    # =====================================================

    def create_plan(
        self,
        state: AgentState
    ) -> AgentState:

        query = state.query.lower()

        state.set_status("planning")

        # Calculator

        if (
            self.calculator_pattern.match(state.query.strip())
            or any(word in query for word in [
                "calculate",
                "compute",
                "solve",
                "evaluate"
            ])
        ):

            state.add_tool("calculator")

        # DateTime

        if any(word in query for word in [
            "date",
            "time",
            "today",
            "day",
            "utc",
            "timestamp"
        ]):

            state.add_tool("datetime")

        # Document Search

        if any(word in query for word in [
            "what",
            "why",
            "how",
            "explain",
            "describe",
            "jwt",
            "redis",
            "fastapi",
            "postgres",
            "python",
            "rag"
        ]):

            state.add_tool("document_search")

        # System Info

        if any(word in query for word in [
            "cpu",
            "ram",
            "memory",
            "disk",
            "system",
            "machine"
        ]):

            state.add_tool("system_info")

        if len(state.planned_tools) == 0:

            state.add_tool("llm")

        state.set_status("planned")

        return state

    # =====================================================
    # LLM Planner
    # =====================================================

    def create_llm_plan(
        self,
        state: AgentState
    ):

        prompt = self.prompt_builder.build_prompt(
            state.query
        )

        messages = [

            {
                "role": "system",
                "content": "You are an AI planner. Return ONLY valid JSON."
            },

            {
                "role": "user",
                "content": prompt
            }

        ]

        start = time.time()

        try:

            response = chat_with_ai(messages)

            latency = round(
                (time.time() - start) * 1000,
                2
            )

            state.add_metadata(
                "planner_latency_ms",
                latency
            )

            return response

        except Exception as e:

            state.add_error(str(e))

            return None

    # =====================================================
    # Parse LLM Response
    # =====================================================

    def parse_llm_plan(
        self,
        response
    ):

        if not response:

            return []

        response = response.strip()

        response = response.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        )

        try:

            data = json.loads(response)

        except Exception:

            return []

        tools = []

        for tool in data.get("tools", []):

            name = tool.get("name")

            if self.registry.tool_exists(name):

                tools.append(name)

        return tools

    # =====================================================
    # Hybrid Planner
    # =====================================================

    def create_dynamic_plan(
        self,
        state: AgentState
    ):

        start = time.perf_counter()

        state.reset()

        planner_type = "rule"

        # ----------------------------
        # Rule Planner
        # ----------------------------

        self.create_plan(state)

        # If only LLM selected, try LLM planner

        if state.planned_tools == ["llm"]:

            planner_type = "llm"

            state.planned_tools.clear()

            response = self.create_llm_plan(state)

            tools = self.parse_llm_plan(response)

            for tool in tools:

                state.add_tool(tool)

            state.add_metadata(
                "raw_llm_response",
                response
            )

        # ----------------------------
        # Validation
        # ----------------------------

        valid_tools, invalid_tools = self.validator.validate(
            state.planned_tools
        )

        state.planned_tools = valid_tools

        if invalid_tools:

            state.add_metadata(
                "invalid_tools",
                invalid_tools
            )

        # ----------------------------
        # Validation Fallback
        # ----------------------------

        if len(state.planned_tools) == 0:

            planner_type = "fallback"

            state.add_tool("llm")

        state.set_status("planned")

        elapsed = time.perf_counter() - start

        PlannerMetadata.update(

            state=state,

            planner_type=planner_type,

            planning_time=elapsed,

            valid_tools=state.planned_tools,

            invalid_tools=invalid_tools

        )
        self.logger.log(state)

        return state

    # =====================================================
    # Utilities
    # =====================================================

    def print_plan(
        self,
        state: AgentState
    ):

        print()

        print("=" * 70)

        print("AGENT EXECUTION PLAN")

        print("=" * 70)

        print("Query:")

        print(state.query)

        print()

        print("Planned Tools:")

        for i, tool in enumerate(
            state.planned_tools,
            start=1
        ):

            print(f"{i}. {tool}")

        print()

    def get_plan(
        self,
        query: str
    ):

        state = AgentState(query=query)

        self.create_dynamic_plan(state)

        return state.planned_tools