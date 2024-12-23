from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QLabel, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor

from conversations.conversation import get_all_conversations, Conversation
from .styles import scroll_bar_style, list_widget_style
from .button import Button
from .resources import NEW_CONVERSATION_ICON_NAME, get_icon, FORK_ICON_NAME, DELETE_ICON_NAME


class Conversations(QVBoxLayout):
    def __init__(self, on_conversation_clicked, on_new_conversation_clicked, on_conversation_deleted):
        super().__init__()
        self.on_conversation_clicked = on_conversation_clicked
        self.on_conversation_deleted = on_conversation_deleted

        self.conversation_list = QListWidget()
        self.conversation_list.itemClicked.connect(self.on_item_clicked)
        all_conversations = get_all_conversations()
        for conversation in all_conversations:
            self.add_conversation(conversation)

        self.conversation_list.setStyleSheet(list_widget_style + scroll_bar_style)
        self.addWidget(self.conversation_list)
        self.addWidget(
            Button("", get_icon(NEW_CONVERSATION_ICON_NAME), "Start new conversation", on_new_conversation_clicked))

    def on_item_clicked(self, item: QListWidgetItem):
        conversation_name = item.data(Qt.ItemDataRole.UserRole).file_name
        self.on_conversation_clicked(conversation_name)

    def fork_conversation(self, filename):
        conversation = Conversation.load(filename).copy()
        conversation.save()
        self.add_conversation(conversation)

    def add_conversation(self, conversation):
        item = QListWidgetItem()
        item.setData(Qt.ItemDataRole.UserRole, conversation)
        item_widget = QWidget()

        conversation_layout = QHBoxLayout()
        label = QLabel(f"{conversation.title}")
        label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        conversation_layout.addWidget(label, 1)
        fork_button = Button("", get_icon(FORK_ICON_NAME), "Fork conversation",
                             lambda _, it=conversation: self.fork_conversation(it.file_name))

        delete_button = Button("", get_icon(DELETE_ICON_NAME), "Delete conversation",
                               lambda _,
                                      it={"filename": conversation.file_name, "item": item}: self.remove_conversation(
                                   it['filename'], it['item']))

        conversation_layout.addWidget(delete_button)
        conversation_layout.addWidget(fork_button)
        item_widget.setLayout(conversation_layout)
        self.conversation_list.addItem(item)
        self.conversation_list.setItemWidget(item, item_widget)

    def remove_conversation(self, filename, item):
        Conversation.delete(filename)
        self.conversation_list.takeItem(self.conversation_list.row(item))
        self.on_conversation_deleted()
