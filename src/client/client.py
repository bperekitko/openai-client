import os

from dotenv import load_dotenv
from openai import OpenAI

from conversations.conversation import Conversation

load_dotenv()


class OpenAiClient:
    __CLIENT_MODEL = "gpt-4o"

    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def send_query(self, conversation):
        completion = self.client.chat.completions.create(
            model=self.__CLIENT_MODEL,
            messages=conversation.messages
        )
        response = completion.choices[0].message.content
        conversation.add_message("assistant", response)
        conversation.tokens_used = completion.usage.total_tokens
        if conversation.title is None:
            completion = self.client.chat.completions.create(
                model=self.__CLIENT_MODEL,
                messages=conversation.messages + [{"role": "user",
                                                                "content": "Create short title for this conversation using language used in the conversation and not more than 30 characters"}]
            )
            conversation.title = completion.choices[0].message.content
        conversation.save()
        return response
