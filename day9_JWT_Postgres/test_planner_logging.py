from app.agents.agent_state import AgentState
from app.agents.planner import Planner

planner = Planner()

queries = [

    "Calculate 250*42",

    "What is JWT?",

    "Show CPU usage",

    "Today's date",

    "Explain AI"

]

for q in queries:

    state = AgentState(query=q)

    planner.create_dynamic_plan(state)

print("Planner logging completed.")