import re

from app.agents.agent_state import AgentState


class Planner:
    """
    Rule-based planner that determines which tools
    should be executed for a user query.
    """

    def __init__(self):

        self.calculator_pattern = re.compile(
            r'^[\d\+\-\*\/\(\)\s\.]+$'
        )

    def create_plan(
        self,
        state: AgentState
    ) -> AgentState:

        query = state.query.lower()

        state.set_status("planning")

        # ---------------- Calculator ----------------

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

        # ---------------- Date & Time ----------------

        if any(word in query for word in [
            "date",
            "time",
            "day",
            "utc",
            "timestamp",
            "today"
        ]):

            state.add_tool("datetime")

        # ---------------- Document Search ----------------

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

        # ---------------- System Info ----------------

        if any(word in query for word in [
            "cpu",
            "ram",
            "memory",
            "system",
            "disk",
            "machine"
        ]):

            state.add_tool("system_info")

        if len(state.planned_tools) == 0:

            state.add_tool("llm")

        state.set_status("planned")

        return state

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

        for i, tool in enumerate(state.planned_tools, start=1):

            print(f"{i}. {tool}")

        print()

    def get_plan(
        self,
        query: str
    ):

        state = AgentState(query=query)

        self.create_plan(state)

        return state.planned_tools