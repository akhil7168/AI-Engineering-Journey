from app.agents.agent_state import AgentState
from app.agents.workflow import WorkflowEngine

state = AgentState(
    query="Calculate 25*16"
)

state.add_tool(
    "calculator"
)

workflow = WorkflowEngine()

workflow.execute(state)

print()

print("=" * 70)

print(state.completed_tools)

print()

print(state.tool_outputs)

print()

print(state.errors)