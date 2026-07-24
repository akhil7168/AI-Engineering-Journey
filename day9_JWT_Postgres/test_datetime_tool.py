from app.tools.datetime_tool import DateTimeTool

tool = DateTimeTool()

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
        tool.execute(
            action=action
        )
    )

    print()