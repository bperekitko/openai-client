from PyQt6 import QtWidgets, QtGui, QtCore
from styles import scroll_bar_style, prompt_query_style
from PyQt6.QtCore import Qt


class AutoExpandingTextEdit(QtWidgets.QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.document().contentsChanged.connect(self.sizeAdjust)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  
        self.setMinimumHeight(40)  # Ustaw minimalną wysokość, jeśli potrzebujesz
        self.setStyleSheet(scroll_bar_style + prompt_query_style)
        self.setContentsMargins(0,0,0,0)
        self.setPlaceholderText("Type your query here...")
        self.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.setWordWrapMode(QtGui.QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
        self.sizeAdjust()

    def sizeAdjust(self):
        doc = self.document()
        calculated_size = int(doc.size().height()) + self.contentsMargins().top() + self.contentsMargins().bottom()
        self.setMaximumHeight(calculated_size if calculated_size <= self.getMaxHeight() else self.getMaxHeight())

    def sizeHint(self):
        # Zwraca sugerowany wymiar dla widgetu
        return QtCore.QSize(self.width(), self.maximumHeight())

    def getMaxHeight(self):
        return 200;
