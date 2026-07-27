from app.agents.llm_planner import LLMPlanner

planner = LLMPlanner()

response = """
{
    "tools":[
        {
            "name":"calculator",
            "arguments":{
                "expression":"25*16"
            }
        },
        {
            "name":"datetime",
            "arguments":{
                "action":"date"
            }
        }
    ]
}
"""

plan = planner.parse_response(response)

print(plan)

print()

print(planner.list_selected_tools(plan))

print()

print(planner.tool_count(plan))