button_style = """
            QPushButton {
                background-color: #3A3A62;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: #7979C6;
            }
            QPushButton:pressed {
                background-color: #3A3A62; 
            } 
            QPushButton:released {
                background-color: #3A3A62;
            }
        """

scroll_bar_style = """
            QScrollBar:vertical {
                border: none;
                background: transparent;
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background-color: #5A5A7A;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical {
                  border: none;
                  background: transparent;
            }
            QScrollBar::sub-line:vertical {
                  border: none;
                  background: transparent;
            }
        """
invisible_scroll = """
    QScrollBar:vertical {
        width: 12px;
        background: transparent;
    }
    QScrollBar::handle:vertical {
        background: transparent;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        border: none;
        background: none;
    }
"""
list_widget_style = """
            QListWidget {
                border: none;
                background-color: #141526;
            }

            QListWidget::item {
                height: 50px;
            }

            QListWidget::item:pressed {
                background-color: #141526;
            }

            QListWidget::item:released {
                background-color: #141526;
            }
            
            QListWidget::item:selected {
                background-color: #25284A;
            }

            QListWidget::item:hover {
                background-color: #25284A;
            }
            """
prompt_query_style = """
     QTextEdit{
                background: transparent;
                padding: 1px;
            }
"""
