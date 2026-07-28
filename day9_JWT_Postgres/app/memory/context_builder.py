from app.memory.memory_manager import MemoryManager


class ContextBuilder:
    """
    Builds context for the LLM using memory.
    """

    def __init__(self):

        self.memory_manager = MemoryManager()

    # =====================================================

    def build_context(
        self,
        query: str
    ):

        memory = self.memory_manager.get_memory()

        summary = memory.get_summary()

        recent_messages = memory.last_messages(6)

        context = []

        # Summary

        if summary:

            context.append({

                "role": "system",

                "content":
                    f"Conversation Summary:\n{summary}"

            })

        # Recent Conversation

        context.extend(recent_messages)

        # Current Query

        context.append({

            "role": "user",

            "content": query

        })

        return context