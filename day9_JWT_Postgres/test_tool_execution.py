from app.agents.tool_registry import execute_tool

print(

    execute_tool(

        "calculator",

        expression="(55+45)*10"

    )

)