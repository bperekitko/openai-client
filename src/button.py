from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtCore import Qt
from styles import button_style

button_font = QFont("Verdana", 10, QFont.Weight.Bold)

class Button(QPushButton):
     def __init__(self, title:str, onclick=None):
        super().__init__(title)
        self.setFont(button_font)
        self.setStyleSheet(button_style)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if onclick != None:
            self.clicked.connect(onclick)
       