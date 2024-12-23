from PyQt6.QtCore import Qt, QObject, pyqtSignal, QThread, QThreadPool, QRunnable, QTimer
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy

from conversations.conversation import Conversation
from .resources import get_resource_path, SPINNER_GIF_NAME
from .styles import scroll_bar_style, assistant_chat_bubble_style, user_chat_bubble_style


class Chat(QScrollArea):
    def __init__(self, on_new_conversation_created):
        super().__init__()
        self.setWidgetResizable(True)
        self.setStyleSheet(scroll_bar_style + "QWidget{background-color: #1E1E2E; border: none;}")
        self.chat_area_widget = QWidget()
        self.area_layout = QVBoxLayout(self.chat_area_widget)
        self.area_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setWidget(self.chat_area_widget)
        self.thread_pool = QThreadPool()
        self.verticalScrollBar().rangeChanged.connect(self.scroll_to_bottom)
        self.conversation = Conversation(None)
        self.on_new_conversation_created = on_new_conversation_created

    def scroll_to_bottom(self):
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

    def set_conversation(self, conversation):
        self.conversation = conversation
        self.clear()
        for msg in self.conversation.messages:
            if msg['role'] == 'system':
                continue
            self.__add_message_sync(msg['content'], msg['role'])

    def clear(self):
        while self.area_layout.count():
            item = self.area_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def add_message(self, query, response_supplier):
        self.conversation.add_message('user', query)
        self.__add_message_sync(query, 'user')
        self.__add_response_async(lambda: response_supplier(self.conversation))

    def __add_message_sync(self, text, role):
        bubble = ChatBubble(text, role)
        self.area_layout.addWidget(bubble)

    def __add_response_async(self, response_supplier):
        loading_widget = LoadingChatBubble()
        self.area_layout.addWidget(loading_widget)
        worker = Worker(response_supplier)
        worker.signals.finished.connect(lambda response: self.stop_loading(response, loading_widget))
        worker.signals.error.connect(lambda error: self.stop_loading(error, loading_widget))
        self.thread_pool.start(worker)

    def stop_loading(self, response, widget):
        self.area_layout.removeWidget(widget)
        bubble = ChatBubble(response, 'assistant')
        self.area_layout.addWidget(bubble)
        if len(self.conversation.messages) == 3:
            self.on_new_conversation_created(self.conversation)

class LoadingChatBubble(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)

        movie = QMovie(get_resource_path(SPINNER_GIF_NAME))
        movie.start()

        label = QLabel()
        label.setMovie(movie)
        label.setStyleSheet(assistant_chat_bubble_style)
        layout.addWidget(label)

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
        label.setStyleSheet(user_chat_bubble_style if sender == "user" else assistant_chat_bubble_style)
        layout.addWidget(label)

class Worker(QRunnable):
    def __init__(self, value_supplier_function):
        super().__init__()
        self.value_supplier_function = value_supplier_function
        self.signals = WorkerSignals()

    def run(self):
        try:
            value = self.value_supplier_function()
            self.signals.finished.emit(value)
        except Exception as exc:
            self.signals.error.emit(str(exc))

class WorkerSignals(QObject):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)