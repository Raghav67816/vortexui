from theme_engine import ThemeEngine
from windows import FMainWindow
from widgets import FButton
from PySide6.QtWidgets import QApplication, QScrollArea, QLabel, QWidget, QGroupBox
from PySide6.QtGui import QFont


class Window(FMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Theme Engine Test")
        self.setMinimumSize(800, 600)
        self.theme_engine = ThemeEngine()
    
        
        # self.scroll_area = QScrollArea()
        # self.scroll_area.setObjectName("scrollArea")
        # self.scroll_area.setWidgetResizable(True)
        # self.scroll_area.setWidget(
            # QLabel(
                # "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            # )
        # )
        # self.layout.addWidget(self.scroll_area)


        self.groupBox = QGroupBox()
        # self.groupBox.setStyleSheet("background-color: white")
        self.layout.addWidget(self.groupBox)

        self.setStyleSheet(
            self.theme_engine.active_scheme(
                self.theme_engine.default_theme
            )
        )
        self.theme_engine.get_scroll_areas(self)

        self.btn = FButton("Hello World")
        self.content_layout.addWidget(self.btn)


app = QApplication()
font = QFont("./fonts/Rajdhani-Regular.ttf")
app.setFont(font)
win = Window()
win.show()
app.exec()
