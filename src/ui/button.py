from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtCore import Qt, QSize
from .styles import button_style


class Button(QPushButton):
    def __init__(self, title: str, icon=None, tooltip=None, onclick=None):
        super().__init__(title)
        self.setFont(QFont("Verdana", 10, QFont.Weight.Bold))
        self.setStyleSheet(button_style)
        if icon != None:
            self.setIcon(icon)
        self.setToolTip(tooltip)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if onclick != None:
            self.clicked.connect(onclick)
