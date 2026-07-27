from app.agents.agent_state import AgentState
from app.agents.planner import Planner

planner = Planner()

state = AgentState(
    query="Calculate 150*25"
)

planner.create_dynamic_plan(state)

print()

print("=" * 80)

print("PLANNED TOOLS")

print(state.planned_tools)

print()

print("=" * 80)

print("METADATA")

for key, value in state.metadata.items():

    print(f"{key}: {value}")