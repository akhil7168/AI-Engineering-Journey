from app.prompts.planner_prompt import PlannerPrompt

planner = PlannerPrompt()

prompt = planner.build_prompt(
    "Explain Redis and calculate 100/5"
)

print(f"Prompt Length: {len(prompt)} characters")
print(f"Prompt Lines : {len(prompt.splitlines())}")