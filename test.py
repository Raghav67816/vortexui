from vortexui.widgets import FButton
from vortexui.windows import FMainWindow, MessageBox
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QFont
from vortexui.theme_engine import ThemeEngine

class SystemMonitorApp(FMainWindow):
    def __init__(self):
        super(SystemMonitorApp, self).__init__()

        self.setMinimumSize(800, 600)

        self.setWindowTitle("Application Test")
        self.theme_engine = ThemeEngine()
        self.setStyleSheet(self.theme_engine.active_scheme(self.theme_engine.default_theme))        

        self.btn = FButton("Open Message Box")
        self.btn.setMinimumSize(100, 40)
        self.btn.setMaximumWidth(200)

        self.btn.connect_func(self.on_btn_click)

        self.about_text = QLabel("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        self.about_text.setWordWrap(True)
        self.add_content(self.about_text)
        self.add_content(self.btn)

    def on_btn_click(self):
        print("button clicked")
        self.msg_box = MessageBox(theme_engine=self.theme_engine, title="Hello")
        self.msg_box.setMinimumSize(500, 250)
        self.msg_box.setMaximumSize(500, 250)

        self.ok = FButton("Ok")
        self.close_btn = FButton("Close")

        self.msg_box.add_btn(self.ok, self.on_ok_clicked)
        self.msg_box.add_btn(self.close_btn, self.on_close_clicked)

        self.text = QLabel("Hello, World! This is a awesome FUI toolkit.")
        self.msg_box.add_content(self.text)

        self.msg_box.show()

    def on_ok_clicked(self):
        print("Ok Clicked")

    def on_close_clicked(self):
        self.msg_box.close()
        


app = QApplication()
font = QFont("vortexui/fonts/Rajdhani-Regular.ttf")
app.setFont(font)
win = SystemMonitorApp()
win.show()
app.exec()