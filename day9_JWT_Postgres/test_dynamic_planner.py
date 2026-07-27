from app.agents.agent_state import AgentState
from app.agents.planner import Planner

planner = Planner()

queries = [

    "Calculate 25*16",

    "What is today's date?",

    "Explain Redis",

    "Calculate 25*16 and explain JWT",

    "Tell me a joke"

]

for query in queries:

    state = AgentState(query=query)

    planner.create_dynamic_plan(state)

    print("=" * 70)

    print(query)

    print()

    print("Planner:")

    print(state.metadata.get("planner"))

    print()

    print("Tools:")

    print(state.planned_tools)

    print()

    print("Metadata:")

    print(state.metadata)

    print()