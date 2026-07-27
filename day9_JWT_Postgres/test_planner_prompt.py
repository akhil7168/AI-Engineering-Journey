from app.prompts.planner_prompt import PlannerPrompt

planner = PlannerPrompt()

prompt = planner.build_prompt(
    "Calculate 25*16 and tell me today's date."
)

print("=" * 80)
print("PLANNER PROMPT")
print("=" * 80)
print()
print(prompt)