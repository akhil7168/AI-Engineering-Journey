from app.agents.tool_registry import execute_tool

actions = [

    "date",

    "time",

    "datetime",

    "utc",

    "day",

    "iso",

    "timestamp"

]

for action in actions:

    print("=" * 70)

    print(

        execute_tool(

            "datetime",

            action=action

        )

    )

    print()

print(

    execute_tool(

        "datetime",

        action="moon"

    )

)