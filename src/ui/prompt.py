from PyQt6.QtWidgets import QTextEdit, QHBoxLayout, QWidget, QFrame, QStackedWidget, QScrollBar, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, QEvent, QPoint
from PyQt6.QtGui import QTextOption
from .button import Button
from .resources import SEND_ICON_NAME, get_icon
from .styles import scroll_bar_style, invisible_scroll
from .auto_resizing_text_edit import AutoExpandingTextEdit


class Prompt(QHBoxLayout):
    def __init__(self, on_prompt_emitted):
        super().__init__()
        self.input = AutoExpandingTextEdit()

        self.scroll_bar = QScrollBar(Qt.Orientation.Vertical)
        self.scroll_bar.setMaximum(self.input.verticalScrollBar().maximum())
        self.input.verticalScrollBar().valueChanged.connect(self.scroll_bar.setValue)
        self.input.textChanged.connect(self.update_scroll_bar)
        self.scroll_bar.valueChanged.connect(self.input.verticalScrollBar().setValue)

        frame_layout = QHBoxLayout()
        send_button = Button(None, get_icon(SEND_ICON_NAME), "Send", self.emitPrompt)
        frame_layout.addWidget(self.input, 1)
        frame_layout.addWidget(send_button, 0, Qt.AlignmentFlag.AlignBottom)
        frame_layout.addWidget(self.scroll_bar)

        frame = QFrame()
        frame.setContentsMargins(0, 0, 0, 0)
        frame.setStyleSheet("QFrame{ border: 1px solid #3A3A62; border-radius: 5px} QTextEdit{border: none;}")
        frame.setLayout(frame_layout)

        self.onPromptEmitted = on_prompt_emitted
        self.input.installEventFilter(self)
        self.addWidget(frame)
        self.update_scroll_bar()

    def update_scroll_bar(self):
        self.scroll_bar.setMaximum(self.input.verticalScrollBar().maximum())
        self.scroll_bar.setPageStep(self.input.verticalScrollBar().pageStep())
        doc_height = self.input.document().size().height()
        if doc_height > self.input.getMaxHeight():
            self.scroll_bar.setStyleSheet(scroll_bar_style)
        else:
            self.scroll_bar.setStyleSheet(invisible_scroll)

    def emitPrompt(self):
        value = self.input.toPlainText().strip()
        if len(value) != 0:
            self.onPromptEmitted(value)
            self.input.clear()

    def eventFilter(self, obj, event):
        if obj == self.input and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
                if event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
                    self.input.insertPlainText("\n")
                    return True
                else:
                    self.emitPrompt()
                    return True
        return False
