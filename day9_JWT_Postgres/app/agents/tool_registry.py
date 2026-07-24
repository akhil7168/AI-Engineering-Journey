from app.tools.calculator import CalculatorTool

from app.tools.datetime_tool import DateTimeTool

from app.tools.search_documents import DocumentSearchTool

from app.tools.system_info import SystemInfoTool


TOOLS = {

    CalculatorTool.name:
        CalculatorTool(),

    DateTimeTool.name:
        DateTimeTool(),

    DocumentSearchTool.name:
        DocumentSearchTool(),

    SystemInfoTool.name:
        SystemInfoTool()
}


def get_tool(name: str):

    return TOOLS.get(name)


def list_tools():

    return [

        tool.info()

        for tool in TOOLS.values()
    ]

def has_tool(name: str):

    return name in TOOLS

def execute_tool(
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
            "error": f"Unknown tool: {tool_name}"
        }

    return tool.execute(**kwargs)