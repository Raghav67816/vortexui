import sys
from PySide6.QtGui import QFont
from widgets import FButton, FProgressBar, FTextInput, FSlider, FTabWidget
from windows import FMainWindow
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout


class MainWindow(FMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setMinimumSize(800, 600)
        self.setWindowTitle("Futuristic User Interface Toolkit")

if __name__ == "__main__":
    app = QApplication()

    font_ = QFont("fonts/Rajdhani-Regular.ttf")
    app.setFont(font_)

    win = MainWindow()
    win.show()
    sys.exit(app.exec())
