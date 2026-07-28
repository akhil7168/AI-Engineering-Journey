from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ConversationMemory:
    """
    Stores conversation history for an AI session.
    """

    messages: List[Dict] = field(default_factory=list)

    summary: str = ""

    # ---------------------------------------------------
    # Add Message
    # ---------------------------------------------------

    def add_message(
        self,
        role: str,
        content: str
    ):

        self.messages.append({

            "role": role,

            "content": content

        })

    # ---------------------------------------------------
    # Get All Messages
    # ---------------------------------------------------

    def get_messages(self):

        return self.messages

    # ---------------------------------------------------
    # Last N Messages
    # ---------------------------------------------------

    def last_messages(
        self,
        n: int = 5
    ):

        return self.messages[-n:]

    # ---------------------------------------------------
    # Remove Last Message
    # ---------------------------------------------------

    def remove_last_message(self):

        if self.messages:

            self.messages.pop()

    # ---------------------------------------------------
    # Clear Memory
    # ---------------------------------------------------

    def clear(self):

        self.messages.clear()

        self.summary = ""

    # ---------------------------------------------------
    # Update Summary
    # ---------------------------------------------------

    def set_summary(
        self,
        summary: str
    ):

        self.summary = summary

    # ---------------------------------------------------
    # Get Summary
    # ---------------------------------------------------

    def get_summary(self):

        return self.summary

    # ---------------------------------------------------
    # Message Count
    # ---------------------------------------------------

    def message_count(self):

        return len(self.messages)

    # ---------------------------------------------------
    # Approximate Token Count
    # ---------------------------------------------------

    def token_count(self):

        total = len(self.summary.split())

        for message in self.messages:

            total += len(

                message["content"].split()

            )

        return total

    # ---------------------------------------------------
    # Convert to Dictionary
    # ---------------------------------------------------

    def to_dict(self):

        return {

            "summary": self.summary,

            "messages": self.messages

        }

    # ---------------------------------------------------
    # Load From Dictionary
    # ---------------------------------------------------

    @classmethod
    def from_dict(
        cls,
        data: dict
    ):

        memory = cls()

        memory.summary = data.get(

            "summary",

            ""

        )

        memory.messages = data.get(

            "messages",

            []

        )

        return memory