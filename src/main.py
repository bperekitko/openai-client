import sys

from PyQt6.QtWidgets import QApplication

from ui.app import ChatGPTApp


def main():
    app = QApplication(sys.argv)
    ex = ChatGPTApp()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
