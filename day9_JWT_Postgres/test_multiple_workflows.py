from app.agents.agent_state import AgentState
from app.agents.planner import Planner
from app.agents.workflow import WorkflowEngine

planner = Planner()

workflow = WorkflowEngine()

queries = [

    "25*10",

    "Today's date",

    "Explain JWT",

    "CPU usage",

    "Calculate 25*8 and explain Redis"

]

for query in queries:

    print()

    print("=" * 80)

    print(query)

    state = AgentState(query=query)

    planner.create_plan(state)

    workflow.execute(state)

    workflow.print_results(state)