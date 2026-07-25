from app.agents.planner import Planner

planner = Planner()

queries = [

    "Calculate 5*6",

    "Explain JWT",

    "Current date",

    "CPU usage",

    "Calculate 8*9 and explain Redis"

]

for query in queries:

    print()

    print(query)

    print(planner.get_plan(query))