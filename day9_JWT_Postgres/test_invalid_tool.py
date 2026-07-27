from app.agents.llm_planner import LLMPlanner

planner = LLMPlanner()

response = """
{
    "tools":[
        {
            "name":"weather",
            "arguments":{}
        },
        {
            "name":"calculator",
            "arguments":{
                "expression":"15*9"
            }
        }
    ]
}
"""

plan = planner.parse_response(response)

print(plan)