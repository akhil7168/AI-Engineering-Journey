from app.agents.agent_state import AgentState

from app.services.agent_state_service import AgentStateService

from app.core.redis import redis_client

state = AgentState(

    query="Calculate 25*16"

)

state.add_tool(

    "calculator"

)

state.complete_tool(

    "calculator"

)

state.add_output(

    "calculator",

    400

)

state.set_response(

    "400"

)

AgentStateService.save_state(

    "demo",

    state

)

loaded = AgentStateService.load_state(

    "demo"

)

print()

print("Loaded State")

print()

print(loaded)

AgentStateService.delete_state(

    "demo"

)