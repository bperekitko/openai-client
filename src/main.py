import sys
from ui.app import ChatGPTApp
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    ex = ChatGPTApp()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
