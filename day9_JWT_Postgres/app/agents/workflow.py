from app.agents.agent_state import AgentState
from app.agents.tool_executor import ToolExecutor


class WorkflowEngine:
    """
    Executes the tools selected by the planner.
    """

    def __init__(self):

        self.executor = ToolExecutor()

    def execute(
        self,
        state: AgentState
    ) -> AgentState:

        state.set_status("executing")

        for tool in state.planned_tools:

            try:

                result = self.execute_tool(
                    tool,
                    state.query
                )

                state.add_output(
                    tool,
                    result
                )

                state.complete_tool(
                    tool
                )

            except Exception as e:

                state.add_error(
                    f"{tool}: {str(e)}"
                )

        if state.errors:

            state.set_status("completed_with_errors")

        else:

            state.set_status("completed")

        return state

    def execute_tool(
        self,
        tool_name: str,
        query: str
    ):

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