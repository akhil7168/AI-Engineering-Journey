from app.agents.agent_state import AgentState
from app.agents.planner import Planner
from app.agents.workflow import WorkflowEngine
from app.agents.response_generator import ResponseGenerator

planner = Planner()

workflow = WorkflowEngine()

generator = ResponseGenerator()

state = AgentState(

    query="Calculate 25*16 and explain JWT"

)

planner.create_plan(state)

workflow.execute(state)

generator.generate(state)

generator.print_response(state)