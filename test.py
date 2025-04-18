import sys
from vortexui.windows import FMainWindow
from PySide6.QtWidgets import QApplication

class Window(FMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        print("All Done")
        self.setWindowTitle("Hello World")


app = QApplication()
win = Window()
win.show()
sys.exit(app.exec())


