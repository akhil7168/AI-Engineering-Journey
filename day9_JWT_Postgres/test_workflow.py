from app.agents.agent_state import AgentState
from app.agents.planner import Planner
from app.agents.workflow import WorkflowEngine

planner = Planner()

workflow = WorkflowEngine()

state = AgentState(

    query="Calculate 25*16 and explain JWT"

)

planner.create_plan(state)

workflow.execute(state)

workflow.print_results(state)

print()

print(state.to_dict())