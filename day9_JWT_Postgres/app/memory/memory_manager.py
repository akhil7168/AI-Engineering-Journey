from app.memory.conversation_memory import ConversationMemory
from app.memory.summarizer import ConversationSummarizer
from app.memory.redis_memory import RedisMemoryStore
class MemoryManager:
    """
    Central manager responsible for maintaining
    conversation memory for an AI session.
    """

    def __init__(self):

        self.memory = ConversationMemory()
        self.summarizer = ConversationSummarizer()
        self.max_messages = 20

        self.max_tokens = 6000

        self.keep_recent_messages = 6

        self.summary_cooldown = 10

        self.messages_since_summary = 0

        self.redis_store = RedisMemoryStore()
    # =====================================================
    # Message Operations
    # =====================================================

    def add_user_message(
    self,
    content
    ):

        self.memory.add_message(
            "user",
            content
    )

        self.messages_since_summary += 1

    def add_assistant_message(
    self,
    content
    ):

        self.memory.add_message(
            "assistant",
            content
    )

        self.messages_since_summary += 1

    # =====================================================
    # Memory Access
    # =====================================================

    def get_memory(self):

        return self.memory

    def get_messages(self):

        return self.memory.get_messages()

    def get_recent_messages(
        self,
        n: int = 6
    ):

        return self.memory.last_messages(n)

    def get_summary(self):

        return self.memory.get_summary()

    # =====================================================
    # Summary Operations
    # =====================================================

    def update_summary(
        self,
        summary: str
    ):

        self.memory.set_summary(summary)

    # =====================================================
    # Context Builder
    # =====================================================

    def build_context(
    self,
    recent_messages: int = 6
    ):

        return {

        "summary": self.memory.get_summary(),

        "recent_messages":

            self.memory.last_messages(
                recent_messages
            ),

        "token_count":

            self.memory.token_count()

    }

    # =====================================================
    # Summarization Decision
    # =====================================================

    def should_summarize(self):

        if self.messages_since_summary < self.summary_cooldown:

            return False

        if self.memory.message_count() >= self.max_messages:

            return True

        if self.memory.token_count() >= self.max_tokens:

            return True

        return False

    # =====================================================
    # Serialization
    # =====================================================

    def save(self):

        return self.memory.to_dict()

    def load(
        self,
        data: dict
    ):

        self.memory = ConversationMemory.from_dict(
            data
        )

    # =====================================================
    # Delete Memory
    # =====================================================

    def delete(self):

        self.memory.clear()

    def summarize_memory(self):
        from app.ai.client import chat_with_ai
        summary = self.summarizer.summarize(
            self.memory.get_messages()
        )

        if summary:
            self.memory.set_summary(summary)

        return summary

    def auto_summarize(self):

        if not self.should_summarize():

            return False

        summary = self.summarize_memory()

        recent = self.memory.last_messages(

            self.keep_recent_messages

        )

        self.memory.clear()

        self.memory.set_summary(summary)

        for message in recent:

            self.memory.add_message(

                message["role"],

                message["content"]

            )

        self.messages_since_summary = 0

        return True

    def memory_statistics(self):

        return {

            "messages":

                self.memory.message_count(),

            "tokens":

                self.memory.token_count(),

            "summary_exists":

                self.memory.get_summary() != "",

            "messages_since_summary":

                self.messages_since_summary

        }

    def optimize(self):

        optimized = self.auto_summarize()

        return {

            "optimized": optimized,

            "statistics":

                self.memory_statistics()

        }

    def save_to_redis(
        self,
        session_id: str
    ):

        self.redis_store.save_memory(

            session_id,

            self.memory


        )

    def load_from_redis(
        self,
        session_id: str
    ):

        self.memory = self.redis_store.load_memory(

            session_id

        )   

    def delete_from_redis(
        self,
        session_id: str
    ):

        self.redis_store.delete_memory(

            session_id
        )

    def save_and_optimize(
        self,
        session_id: str
    ):

        self.optimize()

        self.save_to_redis(
            session_id
        )

    def get_context(
        self,
        query: str
    ):

        from app.memory.context_builder import ContextBuilder

        builder = ContextBuilder()

        builder.memory_manager = self

        return builder.build_context(query)