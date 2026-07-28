from app.memory.memory_manager import MemoryManager

manager = MemoryManager()

for i in range(25):

    manager.add_user_message(

        f"Question {i}"

    )

    manager.add_assistant_message(

        f"Answer {i}"

    )

print("=" * 70)

print("BEFORE")

print("=" * 70)

print(

    manager.memory_statistics()

)

print()

result = manager.optimize()

print("=" * 70)

print("OPTIMIZATION RESULT")

print("=" * 70)

print(result)

print()

print("=" * 70)

print("SUMMARY")

print("=" * 70)

print(

    manager.get_summary()

)

print()

print("=" * 70)

print("AFTER")

print("=" * 70)

print(

    manager.memory_statistics()

)

print()

print("=" * 70)

print("RECENT MESSAGES")

print("=" * 70)

print(

    manager.get_recent_messages()

)