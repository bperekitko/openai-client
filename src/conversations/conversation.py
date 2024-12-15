import glob
import json
import os
import uuid

CONVERSATIONS_SAVE_PATH = os.path.join(os.path.dirname(__file__), 'saved')


class Conversation:
    def __init__(self, title):
        self.file_name = uuid.uuid4()
        self.title = title
        self.messages = []
        self.tokens_used = 0

    def add_message(self, role, content):
        message = {"role": role, "content": content}
        self.messages.append(message)

    def save(self):
        with open(f'{CONVERSATIONS_SAVE_PATH}/{self.file_name}.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.__to_dict(), indent=4))

    def __to_dict(self):
        return {
            "title": self.title,
            "tokens_used": self.tokens_used,
            "messages": self.messages
        }

    def copy(self):
        copy = Conversation(self.title)
        for msg in self.messages:
            copy.add_message(msg['role'], msg['content'])
        copy.tokens_used = self.tokens_used
        return copy

    @staticmethod
    def load(name):
        with open(f'{CONVERSATIONS_SAVE_PATH}/{name}.json', 'r') as file:
            data = json.load(file)
            conversation = Conversation(data['title'])
            conversation.file_name = name
            conversation.messages = data['messages']
            conversation.tokens_used = data['tokens_used']
            return conversation

    @staticmethod
    def delete(filename):
        os.remove(f'{CONVERSATIONS_SAVE_PATH}/{filename}.json')

def get_all_conversations():
    files = glob.glob(os.path.join(CONVERSATIONS_SAVE_PATH, "*.json"))
    files.sort(key=lambda x: os.path.getctime(x))
    file_names = [os.path.splitext(os.path.basename(file))[0] for file in files]

    return [
        Conversation.load(file_name) for file_name in file_names
    ]
