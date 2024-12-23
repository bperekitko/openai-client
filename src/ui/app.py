from PyQt6.QtGui import QColor, QPalette, QGuiApplication, QCursor
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget

from client.client import OpenAiClient
from conversations.conversation import Conversation
from .chat import Chat
from .conversations import Conversations
from .prompt import Prompt


class ChatGPTApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.client = OpenAiClient()
        self.conversations = Conversations(self.on_conversation_changed, self.on_new_conversation_clicked, self.on_new_conversation_clicked)
        self.chat = Chat(lambda conversation: self.conversations.add_conversation(conversation))
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ChatGPT Desktop App")
        cursor_pos = QCursor.pos()
        screen = QGuiApplication.screenAt(cursor_pos)
        geometry = screen.geometry()
        geometry.setX(geometry.x() + 200)
        geometry.setY(geometry.y() + 200)
        geometry.setWidth(1200)
        geometry.setHeight(800)
        self.setGeometry(geometry)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1E1E2E"))
        palette.setColor(QPalette.ColorRole.Base, QColor("#141526"))
        self.setPalette(palette)

        prompt = Prompt(on_prompt_emitted=self.send_query)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.chat, 1)
        right_layout.addLayout(prompt)

        main_layout = QHBoxLayout()
        main_layout.addLayout(self.conversations, 2)
        main_layout.addLayout(right_layout, 5)
        main_layout.setContentsMargins(10,10,10,5)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def on_conversation_changed(self, conversation_name):
        conversation = Conversation.load(conversation_name)
        self.chat.set_conversation(conversation)

    def on_new_conversation_clicked(self):
        self.chat.set_conversation(Conversation(None))

    def send_query(self, query):
        self.chat.add_message(query, lambda conversation: self.client.send_query(conversation))
