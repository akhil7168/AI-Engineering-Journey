from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class AgentState:
    """
    Shared state for the AI Agent workflow.
    """

    query: str

    current_step: int = 0

    status: str = "initialized"

    planned_tools: List[str] = field(default_factory=list)

    completed_tools: List[str] = field(default_factory=list)

    tool_outputs: Dict[str, Any] = field(default_factory=dict)

    errors: List[str] = field(default_factory=list)

    final_response: str = ""

    metadata: Dict[str, Any] = field(default_factory=dict)

    def set_status(
        self,
        status: str
    ):

        self.status = status

    def add_tool(
        self,
        tool_name: str
    ):

        self.planned_tools.append(tool_name)

    def complete_tool(
        self,
        tool_name: str
    ):

        self.completed_tools.append(tool_name)

        self.current_step += 1

    def add_output(
        self,
        tool_name: str,
        output
    ):

        self.tool_outputs[tool_name] = output

    def add_error(
        self,
        error: str
    ):

        self.errors.append(error)

    def set_response(
        self,
        response: str
    ):

        self.final_response = response

    def add_metadata(
        self,
        key: str,
        value
    ):

        self.metadata[key] = value

    def to_dict(self):

        return {

            "query": self.query,

            "current_step": self.current_step,

            "status": self.status,

            "planned_tools": self.planned_tools,

            "completed_tools": self.completed_tools,

            "tool_outputs": self.tool_outputs,

            "errors": self.errors,

            "final_response": self.final_response,

            "metadata": self.metadata

        }
    
    def reset(self):

            self.current_step = 0

            self.status = "initialized"

            self.planned_tools.clear()

            self.completed_tools.clear()

            self.tool_outputs.clear()

            self.errors.clear()

            self.final_response = ""

            self.metadata.clear()