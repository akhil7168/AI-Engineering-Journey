from app.agents.agent_state import AgentState

state = AgentState(

    query="Calculate 55*88 and explain JWT"

)

print("=" * 80)
print("INITIAL STATE")
print("=" * 80)

print(state.to_dict())

state.set_status("planning")

state.add_tool("calculator")

state.add_tool("document_search")

state.complete_tool("calculator")

state.add_output(

    "calculator",

    4840

)

state.complete_tool(

    "document_search"

)

state.add_output(

    "document_search",

    "JWT uses signed tokens."

)

state.set_response(

    "4840\n\nJWT uses signed tokens."

)

print()

print("=" * 80)
print("UPDATED STATE")
print("=" * 80)

print(state.to_dict())