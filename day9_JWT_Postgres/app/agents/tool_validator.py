from app.agents.tool_registry import ToolRegistry


class ToolValidator:
    """
    Validates planner-generated tools before execution.
    """

    def __init__(self):

        self.registry = ToolRegistry()

    def validate(self, planned_tools):

        valid_tools = []

        invalid_tools = []

        seen = set()

        for tool in planned_tools:

            if tool in seen:
                continue

            seen.add(tool)

            if self.registry.tool_exists(tool):

                valid_tools.append(tool)

            else:

                invalid_tools.append(tool)

        return valid_tools, invalid_tools