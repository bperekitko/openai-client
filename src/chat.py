from PyQt6.QtWidgets import QTextEdit
from styles import scroll_bar_style


class Chat(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setPlaceholderText("Here will be the response from ChatGPT...")
        self.setStyleSheet(scroll_bar_style + "QTextEdit{background-color: #1E1E2E; border: none;}")

    def update(self, text):
        self.append(text)
