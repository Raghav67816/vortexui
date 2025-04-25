import sys
from .widgets import FButton, TitleBar
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QFont

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFrame, QSizePolicy, QHBoxLayout, QLabel, QApplication, QDialog, QPushButton

class FMainWindow(QMainWindow):
    def __init__(self):
        super(FMainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.default_size = QSize(self.width(), self.height())

        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        self.content_layout = QVBoxLayout()
        self.content_layout.setSpacing(5)
        self.content_layout.setContentsMargins(9, 9, 9, 9)

        self.central_widget.setLayout(self.layout)

        self.title_bar = TitleBar(window=self)
        self.title_bar.setObjectName("title_bar")

        self.setCentralWidget(self.central_widget)
        self.layout.addWidget(self.title_bar)

        self.layout.addLayout(self.content_layout)

        # self.win_expose_event()

    def setWindowTitle(self, title: str):
        self.title_bar.title_text.setText(title)

    def add_content(self, content: QWidget):
        self.content_layout.addWidget(content)

class Application:
    def __init__(self, window):
        self.app = QApplication([])

        font = QFont("fonts/Rajdhani-Regular.ttf")
        self.app.setFont(font)

        self.window = window
        self.window.show()
        self.app.exec()  # no need for sys.exit()

"""
Message Box
"""
class MessageBox(QDialog):
    def __init__(self, theme_engine, title: str):
        super(MessageBox, self).__init__()


        # default window setup 
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.layout = QVBoxLayout(self)
        self.theme_engine = theme_engine

        self.title_bar = TitleBar(self)
        self.title_bar.setTitle_(title)
        self.title_bar.title_text.setText(title)
        self.title_bar.setObjectName('title_bar')

        # hide maximise and minimise button
        self.title_bar.win_state_btn.deleteLater()
        self.title_bar.hide_win_btn.deleteLater()
        
        self.layout.addWidget(self.title_bar)

        self.setStyleSheet(
            self.theme_engine.active_scheme(
                self.theme_engine.default_theme
            )
        )

        # btns and functions
        # standard buttons
        self.std_btns = []
        self.funcs = []

        # content layout
        self.content_layout = QVBoxLayout()
        self.btn_box_layout = QHBoxLayout()

        self.content_layout.setSpacing(8)
        self.content_layout.setContentsMargins(9, 9, 9, 9)

        self.btn_box_layout.setSpacing(8)
        self.btn_box_layout.setContentsMargins(9, 9, 9, 9)


        self.layout.addLayout(self.content_layout)
        self.layout.addStretch(1)
        self.layout.addLayout(self.btn_box_layout)

    
    def add_content(self, content: QWidget):
        self.content_layout.addWidget(content)

    def add_btn(self, btn: FButton, func: callable):
        self.std_btns.append(btn)
        self.funcs.append(func)


    def show(self):
        if len(self.std_btns) != len(self.funcs):
            raise Exception(f"Button and Function Mismatch: Buttons - {len(self.std_btns)} : {len(self.funcs)}")
        
        # bind functions to buttons
        for index, btn in enumerate(self.std_btns):
            print(f"Type of button: {type(btn)}")
            btn.connect_func(self.funcs[index])
            self.btn_box_layout.addWidget(btn)
            self.btn_box_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        super().show()
