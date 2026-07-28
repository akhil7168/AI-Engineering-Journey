from app.memory.memory_manager import MemoryManager

manager = MemoryManager()

for i in range(15):

    manager.add_user_message(

        f"User question {i}"

    )

    manager.add_assistant_message(

        f"Assistant answer {i}"

    )

print("=" * 70)

print("Messages Before")

print("=" * 70)

print(

    manager.get_memory().message_count()

)

summary = manager.summarize_memory()

print()

print("=" * 70)

print("Generated Summary")

print("=" * 70)

print(summary)

print()

print("=" * 70)

print("Stored Summary")

print("=" * 70)

print(

    manager.get_summary()

)