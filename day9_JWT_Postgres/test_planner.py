from app.agents.agent_state import AgentState
from app.agents.planner import Planner

planner = Planner()

queries = [

    "25*4",

    "What is Redis?",

    "Current time",

    "CPU usage",

    "Calculate 88*44 and today's date",

    "Explain JWT and FastAPI"

]

for q in queries:

    print("=" * 80)

    state = AgentState(query=q)

    planner.create_plan(state)

    planner.print_plan(state)