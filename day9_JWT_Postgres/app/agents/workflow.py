from app.agents.agent_state import AgentState
from app.agents.tool_executor import ToolExecutor
from app.agents.tool_registry import ToolRegistry


class WorkflowEngine:
    """
    Executes the tools selected by the Planner.
    """

    def __init__(self):

        self.registry = ToolRegistry()
        self.executor = ToolExecutor()

    # =====================================================
    # Main Workflow
    # =====================================================

    def execute(
        self,
        state: AgentState
    ):

        state.set_status("executing")

        for tool in state.planned_tools:

            try:

                self.registry.execute_tool(
                    tool,
                    self,
                    state
                )

            except Exception as e:

                state.add_error(str(e))

        state.set_status("completed")

        return state

    # =====================================================
    # Tool Executor Wrapper
    # =====================================================

    def execute_tool(
        self,
        tool_name: str,
        query: str = ""
    ):

        query = query or ""

        # ---------------- Calculator ----------------

        if tool_name == "calculator":

            expression = (
                query.replace("Calculate", "")
                     .replace("calculate", "")
                     .strip()
            )

            return self.executor.execute(
                tool_name="calculator",
                expression=expression
            )

        # ---------------- DateTime ----------------

        elif tool_name == "datetime":

            lower = query.lower()

            if "utc" in lower:

                action = "utc"

            elif "date" in lower:

                action = "date"

            elif "day" in lower:

                action = "day"

            elif "timestamp" in lower:

                action = "timestamp"

            elif "iso" in lower:

                action = "iso"

            else:

                action = "time"

            return self.executor.execute(
                tool_name="datetime",
                action=action
            )

        # ---------------- Document Search ----------------

        elif tool_name == "document_search":

            return self.executor.execute(
                tool_name="document_search",
                query=query
            )

        # ---------------- System Info ----------------

        elif tool_name == "system_info":

            return self.executor.execute(
                tool_name="system_info"
            )

        # ---------------- LLM ----------------

        elif tool_name == "llm":

            return {
                "success": True,
                "tool": "llm",
                "output": None
            }

        raise ValueError(
            f"Unknown tool: {tool_name}"
        )

    # =====================================================
    # Individual Tool Runners
    # =====================================================

    def run_calculator(
        self,
        state: AgentState
    ):

        result = self.execute_tool(
            "calculator",
            state.query
        )

        state.complete_tool("calculator")

        state.add_output(
            "calculator",
            result
        )

    def run_datetime(
        self,
        state: AgentState
    ):

        result = self.execute_tool(
            "datetime",
            state.query
        )

        state.complete_tool("datetime")

        state.add_output(
            "datetime",
            result
        )

    def run_document_search(
        self,
        state: AgentState
    ):

        result = self.execute_tool(
            "document_search",
            state.query
        )

        state.complete_tool("document_search")

        state.add_output(
            "document_search",
            result
        )

    def run_system_info(
        self,
        state: AgentState
    ):

        result = self.execute_tool(
            "system_info",
            state.query
        )

        state.complete_tool("system_info")

        state.add_output(
            "system_info",
            result
        )

    def run_llm(
        self,
        state: AgentState
    ):

        result = self.execute_tool(
            "llm",
            state.query
        )

        state.complete_tool("llm")

        state.add_output(
            "llm",
            result
        )

    # =====================================================
    # Debug Printing
    # =====================================================

    def print_results(
        self,
        state: AgentState
    ):

        print()

        print("=" * 80)
        print("WORKFLOW RESULTS")
        print("=" * 80)

        print("Status:")
        print(state.status)

        print()

        print("Completed Tools:")

        for tool in state.completed_tools:

            print(f"- {tool}")

        print()

        print("Outputs:")

        for tool, output in state.tool_outputs.items():

            print()

            print(tool)
            print(output)

        if state.errors:

            print()

            print("Errors:")

            for error in state.errors:

                print(error)