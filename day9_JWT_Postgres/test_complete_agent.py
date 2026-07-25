from app.agents.agent_state import AgentState
from app.agents.planner import Planner
from app.agents.workflow import WorkflowEngine
from app.agents.response_generator import ResponseGenerator

planner = Planner()

workflow = WorkflowEngine()

generator = ResponseGenerator()

queries = [

    "25*5",

    "Today's date",

    "Explain Redis",

    "CPU usage",

    "Calculate 55*88 and explain JWT"

]

for query in queries:

    print()

    print("=" * 80)

    print(query)

    print("=" * 80)

    state = AgentState(query=query)

    planner.create_plan(state)

    workflow.execute(state)

    generator.generate(state)

    generator.print_response(state)