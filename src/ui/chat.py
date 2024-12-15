from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy

from .styles import scroll_bar_style


class Chat(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)
        self.setStyleSheet(scroll_bar_style + "QWidget{background-color: #1E1E2E; border: none;}")
        self.chat_area_widget = QWidget()
        self.area_layout = QVBoxLayout(self.chat_area_widget)
        self.area_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setWidget(self.chat_area_widget)

    def set_conversation(self, conversation):
        self.clear()
        for msg in conversation.messages:
            if msg['role'] == 'system':
                continue
            self.add_message(msg['content'], msg['role'])

    def clear(self):
        while self.area_layout.count():
            item = self.area_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def add_message(self, text, sender="user"):
        self.area_layout.addWidget(ChatBubble(text, sender))
        self.verticalScrollBar().setValue(
            self.verticalScrollBar().maximum()
        )


class ChatBubble(QWidget):
    def __init__(self, text, sender="user"):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setAlignment(Qt.AlignmentFlag.AlignRight if sender == "user" else Qt.AlignmentFlag.AlignLeft)
        label = QLabel(text)
        label.setWordWrap(True)
        label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        label.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        label.setStyleSheet("""
                        QLabel {
                            background-color: #141526;
                            border-radius: 10px;
                            border: 1px solid black;
                            padding: 10px;  
                        }
                    """)
        layout.addWidget(label)
