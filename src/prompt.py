from PyQt6.QtWidgets import QTextEdit, QHBoxLayout
from PyQt6.QtCore import Qt, QEvent

from button import Button

class Prompt(QHBoxLayout):
    def __init__(self, on_prompt_emitted):
        super().__init__()
        self.input = QTextEdit()
        self.input.setPlaceholderText("Type your query here...")
        self.input.textChanged.connect(self.adjustInputHeight)
        self.input.setMinimumHeight(30)
        self.input.setMaximumHeight(300)
        self.input.setFixedHeight(30)
        self.addWidget(self.input, 1)
        self.addWidget(Button("Send", self.emitPrompt))
        self.onPromptEmitted = on_prompt_emitted
        self.input.installEventFilter(self)

    def emitPrompt(self):
        self.onPromptEmitted(self.input.toPlainText().strip())
        self.input.clear()

    def adjustInputHeight(self):
        print("here should be the calculation of optimal height?")

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
