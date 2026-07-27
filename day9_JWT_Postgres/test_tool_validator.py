from app.agents.tool_validator import ToolValidator

validator = ToolValidator()

tools = [
    "calculator",
    "datetime",
    "weather",
    "calculator",
    "abc",
    "system_info"
]

valid, invalid = validator.validate(tools)

print("Valid Tools:")
print(valid)

print()

print("Invalid Tools:")
print(invalid)