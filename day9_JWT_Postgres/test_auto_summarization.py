from app.memory.memory_manager import MemoryManager

manager = MemoryManager()

for i in range(25):

    manager.add_user_message(

        f"Question {i}"

    )

    manager.add_assistant_message(

        f"Answer {i}"

    )

print(

    manager.should_summarize()

)

manager.auto_summarize()

print()

print(manager.get_summary())

print()

print(

    manager.get_memory().message_count()

)