from PyQt6.QtGui import QColor, QPalette, QGuiApplication, QCursor
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget

from conversations.conversation import Conversation
from .chat import Chat
from .conversations import Conversations
from .prompt import Prompt


class ChatGPTApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chat = Chat()
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

        left_layout = Conversations(lambda filename: self.chat.set_conversation(Conversation.load(filename)))

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(right_layout, 5)
        main_layout.setContentsMargins(10,10,10,5)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def send_query(self, query):
        response = "This is a simulated response to: " + query
        print(response)
        # self.chat.set_conversation(response)
