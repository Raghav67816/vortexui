import sys
from . import styles
from .widgets import FButton, TitleBar
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QSize
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QDialog, QMainWindow, QVBoxLayout, QWidget, QFrame, QSizePolicy, QHBoxLayout, QLabel, QApplication


class FMainWindow(QMainWindow):
    def __init__(self):
        super(FMainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(styles.FWINDOW)

        self.default_size = QSize(self.width(), self.height())

        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.title_bar = TitleBar(self)

        self.setCentralWidget(self.central_widget)
        self.layout.addWidget(self.title_bar)
        self.win_expose_event()

    def setWindowTitle(self, title: str):
        self.title_bar.title_text.setText(title)

    def win_expose_event(self):
        start_geometry = QRect(self.x(), self.y(), 0, self.height())
        end_geometry = QRect(self.x(), self.y(), 800, self.height())
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(15000)  # or 5000 for 5 seconds
        self.anim.setStartValue(start_geometry)
        self.anim.setEndValue(end_geometry)
        self.anim.start()

class Application:
    def __init__(self, window):
        self.app = QApplication([])

        font = QFont("fonts/Rajdhani-Regular.ttf")
        self.app.setFont(font)

        self.window = window
        self.window.show()
        self.app.exec()  # no need for sys.exit()
