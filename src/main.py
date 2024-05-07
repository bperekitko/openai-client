import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QColor, QPalette, QGuiApplication, QScreen, QCursor
from PyQt6.QtCore import QPoint
from chat import Chat
from conversations import Conversations
from prompt import Prompt

class ChatGPTApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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
        
        self.chat = Chat()
        prompt = Prompt(on_prompt_emitted=self.send_query)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.chat, 1)
        right_layout.addLayout(prompt)

        left_layout = Conversations()
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(right_layout, 5)
        main_layout.setContentsMargins(0,0,0,0)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def send_query(self, query):
        response = "This is a simulated response to: " + query
        self.chat.update(response)


def main():
    app = QApplication(sys.argv)
    ex = ChatGPTApp()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
