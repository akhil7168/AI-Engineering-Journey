from typing import Dict


class ToolRegistry:
    """
    Central registry for all tools available
    to the AI agent.
    """

    def __init__(self):

        self.tools = {

            "calculator": {

                "name": "calculator",

                "description":
                    "Perform mathematical calculations.",

                "parameters": {

                    "expression": "string"

                }

            },

            "datetime": {

                "name": "datetime",

                "description":
                    "Retrieve current date and time.",

                "parameters": {

                    "action": "string"

                }

            },

            "document_search": {

                "name": "document_search",

                "description":
                    "Search the knowledge base.",

                "parameters": {

                    "query": "string"

                }

            },

            "system_info": {

                "name": "system_info",

                "description":
                    "Retrieve CPU, RAM, Disk and machine information.",

                "parameters": {}

            },

            "llm": {

                "name": "llm",

                "description":
                    "General AI response.",

                "parameters": {}

            }

        }

    # =====================================================
    # Registry Methods
    # =====================================================

    def get_tool(
        self,
        tool_name: str
    ):

        return self.tools.get(tool_name)

    def get_all_tools(self):

        return self.tools

    def tool_exists(
        self,
        tool_name: str
    ):

        return tool_name in self.tools

    def list_tool_names(self):

        return list(self.tools.keys())

    def get_tool_descriptions(self):

        descriptions = []

        for tool in self.tools.values():

            descriptions.append({

                "name": tool["name"],

                "description": tool["description"]

            })

        return descriptions

    def get_llm_prompt(self):

        prompt = ""

        for tool in self.tools.values():

            prompt += f"""
Tool Name:
{tool["name"]}

Description:
{tool["description"]}

Parameters:
{tool["parameters"]}

"""

        return prompt.strip()

    # =====================================================
    # Dynamic Dispatcher
    # =====================================================

    def execute_tool(
        self,
        tool_name: str,
        workflow,
        state
    ):

        handlers = {

            "calculator": workflow.run_calculator,

            "datetime": workflow.run_datetime,

            "document_search": workflow.run_document_search,

            "system_info": workflow.run_system_info,

            "llm": workflow.run_llm

        }

        handler = handlers.get(tool_name)

        if handler is None:

            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        return handler(state)


# =====================================================
# Backward Compatibility
# =====================================================

_registry = ToolRegistry()


def get_tool(tool_name: str):
    return _registry.get_tool(tool_name)


def get_all_tools():
    return _registry.get_all_tools()


def tool_exists(tool_name: str):
    return _registry.tool_exists(tool_name)


def list_tool_names():
    return _registry.list_tool_names()