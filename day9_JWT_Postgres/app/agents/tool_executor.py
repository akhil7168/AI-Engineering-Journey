from app.agents.tool_registry import get_tool


class ToolExecutor:

    def execute(
        self,
        tool_name: str,
        **kwargs
    ):
        """
        Execute a registered tool.
        """

        tool = get_tool(tool_name)

        if tool is None:

            return {

                "success": False,

                "tool": tool_name,

                "error": "Tool not found."

            }

        try:

            result = tool.execute(**kwargs)

            return {

                "success": True,

                "tool": tool_name,

                "output": result

            }

        except Exception as e:

            return {

                "success": False,

                "tool": tool_name,

                "error": str(e)

            }