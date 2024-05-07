from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QLabel, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from styles import scroll_bar_style, list_widget_style
from button import Button


class Conversations(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.conversation_list = QListWidget()
        self.conversation_list.itemClicked.connect(self.on_item_clicked)

        for i in range(0, 9):
            item = QListWidgetItem()
            data = {"filename": f"file_name {i + 1}"}
            item.setData(Qt.ItemDataRole.UserRole, data)
            self.conversation_list.addItem(item)
            label = QLabel(f"Element {i+1}")
            label.setContentsMargins(10, 10, 10, 10)
            label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.conversation_list.addItem(item)
            conversation_layout = QHBoxLayout()
            conversation_layout.addWidget(label, 1)
            conversation_layout.addWidget(Button("Fork me", lambda _, data=data: print(f"Forking conversation: {data['filename']}")))
            item_widget = QWidget()
            item_widget.setLayout(conversation_layout)
            self.conversation_list.setItemWidget(item, item_widget)

        self.conversation_list.setStyleSheet(list_widget_style + scroll_bar_style)
        self.start_new_button = Button("Start New Conversation")
        self.addWidget(self.conversation_list)
        self.addWidget(self.start_new_button)

    def on_item_clicked(self, item: QListWidgetItem):
        print(f"Kliknięto element: {item.data(Qt.ItemDataRole.UserRole)}")
