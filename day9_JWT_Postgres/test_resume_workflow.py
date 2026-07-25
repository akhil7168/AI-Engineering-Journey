from app.services.agent_state_service import AgentStateService

state = AgentStateService.load_state(

    "workflow"

)

print()

print(state)