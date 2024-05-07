button_style = """
            QPushButton {
                background-color: #3A3A62;
                color: white;
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
                background-color: transparent;
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background-color: #5A5A7A;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical {
                  border: none;
                  background: none;
            }
            QScrollBar::sub-line:vertical {
                  border: none;
                  background: none;
            }
        """

list_widget_style = """
            QListWidget {
                border: none;
                color: white;
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
