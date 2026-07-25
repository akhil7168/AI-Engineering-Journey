from app.agents.agent_state import AgentState

state = AgentState(

    query="Explain Redis"

)

state.add_tool(

    "document_search"

)

state.complete_tool(

    "document_search"

)

state.add_output(

    "document_search",

    "Redis is an in-memory data store."

)

print("Before Reset")

print(state.to_dict())

print()

state.reset()

print("After Reset")

print(state.to_dict())