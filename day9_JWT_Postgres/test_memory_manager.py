from app.memory.memory_manager import MemoryManager

manager = MemoryManager()

manager.add_user_message(
    "Hello"
)

manager.add_assistant_message(
    "Hi! How can I help you?"
)

manager.add_user_message(
    "Explain JWT Authentication."
)

manager.add_assistant_message(
    "JWT is a stateless authentication mechanism."
)

print("=" * 70)

print("MESSAGES")

print("=" * 70)

print(manager.get_messages())

print()

manager.update_summary(

    "User greeted the assistant and learned about JWT."

)

print("=" * 70)

print("SUMMARY")

print("=" * 70)

print(manager.get_summary())

print()

print("=" * 70)

print("RECENT")

print("=" * 70)

print(manager.get_recent_messages(2))

print()

print("=" * 70)

print("CONTEXT")

print("=" * 70)

print(manager.build_context())

print()

print("=" * 70)

print("SAVE")

print("=" * 70)

saved = manager.save()

print(saved)

print()

print("=" * 70)

print("DELETE")

print("=" * 70)

manager.delete()

print(manager.get_messages())

print()

print("=" * 70)

print("RESTORE")

print("=" * 70)

manager.load(saved)

print(manager.get_messages())

print()

print("=" * 70)

print("SHOULD SUMMARIZE")

print("=" * 70)

print(manager.should_summarize())