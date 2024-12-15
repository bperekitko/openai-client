import os

from dotenv import load_dotenv
from openai import OpenAI

from conversations.conversation import Conversation

load_dotenv()


class OpenAiClient:
    __CLIENT_MODEL = "gpt-4o"
    __DEFAULT_ASSISTANT_DESCRIPTION = "You are a helpful assistant"

    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.current_conversation: Conversation | None = None

    def set_conversation(self, conversation: Conversation):
        self.current_conversation = conversation

    def start_new_conversation(self):
        self.current_conversation = Conversation(None)
        self.current_conversation.add_message("system", self.__DEFAULT_ASSISTANT_DESCRIPTION)

    def send_query(self, query):
        self.current_conversation.add_message("user", query)
        completion = self.client.chat.completions.create(
            model=self.__CLIENT_MODEL,
            messages=self.current_conversation.messages
        )
        self.current_conversation.add_message("assistant", completion.choices[0].message.content)
        self.current_conversation.tokens_used = completion.usage.total_tokens
        if self.current_conversation.title is None:
            completion = self.client.chat.completions.create(
                model=self.__CLIENT_MODEL,
                messages=self.current_conversation.messages + [{"role": "user",
                                                                "content": "Create short title for this conversation using language used in the conversation and not more than 30 characters"}]
            )
            self.current_conversation.title = completion.choices[0].message.content
        self.current_conversation.save()
