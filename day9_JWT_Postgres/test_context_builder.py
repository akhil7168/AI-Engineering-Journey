from app.memory.memory_manager import MemoryManager

manager = MemoryManager()

manager.add_user_message(

    "Hello"

)

manager.add_assistant_message(

    "Hi! Nice to meet you."

)

manager.add_user_message(

    "Explain JWT."

)

manager.update_summary(

    "The user greeted the assistant and later asked about JWT."

)

context = manager.get_context(

    "How does refresh token work?"

)

print()

print("=" * 70)

print("LLM CONTEXT")

print("=" * 70)

for message in context:

    print(message)

    print()