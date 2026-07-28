class ConversationSummarizer:
    """
    Summarizes long conversations using the LLM.
    """

    def __init__(self):

        self.system_prompt = """
You are an AI conversation summarizer.

Your job is to create a concise summary of the conversation.

Rules:

- Keep important facts.
- Preserve user goals.
- Preserve technical decisions.
- Remove greetings and small talk.
- Maximum 250 words.

Return only the summary.
"""

    def summarize(
        self,
        messages
    ):
        from app.ai.client import chat_with_ai

        if not messages:

            return ""

        conversation = ""

        for message in messages:

            role = message["role"].capitalize()

            conversation += f"{role}: {message['content']}\n"

        prompt = f"""
Summarize the following conversation.

Conversation:

{conversation}
"""

        llm_messages = [

            {
                "role": "system",
                "content": self.system_prompt
            },

            {
                "role": "user",
                "content": prompt
            }

        ]

        try:

            summary = chat_with_ai(llm_messages)

            return summary.strip()

        except Exception:

            return ""