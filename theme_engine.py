from json import load
from getpass import getuser
from .windows import FMainWindow
from os import path, mkdir, listdir
from PySide6.QtWidgets import QScrollArea, QCheckBox, QTableWidget

class ThemeEngine:
    def __init__(self):
        super(ThemeEngine, self).__init__()

        self.default_path = f"/home/{getuser()}/tars"
        self.default_theme = "default-blue"
        self.check_folder()
        self.get_themes()

        self.active_colors = {}

    # if folder does not exist create a new folder
    def check_folder(self):
        if path.exists(self.default_path) == False:
            mkdir(self.default_path)
            print("folder ready")
            
        else:
            pass

    def get_themes(self) -> list[str]:
        files = listdir(self.default_path)
        for i, file in enumerate(files):
            file = file.split(".")[0]
            files[i] = file
        #self.default_theme = files[0]
        return files

    def active_scheme(self, theme_name: str) -> dict:
        with open(f"{self.default_path}/{theme_name}.json", "r") as active_theme:
            theme = load(active_theme)
            active_theme.close()
            self.active_colors = theme

        with open(f"{self.default_path}/base.css", "r") as base_style_file:
            base_style = base_style_file.read()
            base_style_file.close()


        base_style = base_style.replace("$primary-blue", str(theme['primary-blue']))
        base_style = base_style.replace("$secondary-blue", str(theme['secondary-blue']))
        base_style = base_style.replace("$font-name", str(theme['font-name']))
        base_style = base_style.replace("$family_name", str(theme['family-name']))
        base_style = base_style.replace("$warn-yellow", str(theme['warn-yellow']))
        base_style = base_style.replace("$danger-red", str(theme['danger-red']))
        
        return base_style

    def get_scroll_areas(self, window: FMainWindow):
        test_scroll_area = QScrollArea()
        children = window.findChildren(type(test_scroll_area))
        del test_scroll_area

        # generate style for scroll areas
        style_scroll_area = """
            background-color: transparent
        """

        style_scroll_bar = """
            QScrollBar:vertical, QScrollBar:horizontal {
                background: transparent;
                border: 1px solid $primary-blue;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background: $primary-blue;
                
                min-height: 30px;
                min-width: 20px;
            }

            QScrollBar::handle:vertical::hover{
                background-color: $secondary-blue
            }
            
            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
                border: none;
                width: 0px;
                height: 0px;
            }
            
            QScrollBar::add-page, QScrollBar::sub-page {
                background: black;
            }
        """
        style_scroll_bar = style_scroll_bar.replace(
            "$primary-blue", self.active_colors['primary-blue']
        )
        style_scroll_bar = style_scroll_bar.replace(
            "$secondary-blue", self.active_colors['secondary-blue']
        )

        for child in children:
            child.setStyleSheet(style_scroll_area)
            child.horizontalScrollBar().setStyleSheet(style_scroll_bar)
            child.verticalScrollBar().setStyleSheet(style_scroll_bar)

    def get_check_boxes(self, window: FMainWindow):
        test_check_box = QCheckBox()
        children = window.findChildren(type(test_check_box))
        del test_check_box

        for child in children:
            child.setStyleSheet(
                "QCheckBox::indicator{background-color: $primary-blue; border: 1px solid $secondary-blue; height: 20px; width: 20px;} QCheckBox::indicator::unchecked{background-color: $primary-blue;} QCheckBox::indicator::checked{background-color: $secondary-blue}".replace(
                    "$primary-blue", self.active_colors['primary-blue']
                ).replace("$secondary-blue", self.active_colors['secondary-blue'])
            )

    def get_table_widgets(self, window: FMainWindow):
        test_table_widget = QTableWidget()
        children = window.findChildren(type(test_table_widget))

        del test_table_widget

        for child in children:
            print(child.objectName)
            child.setStyleSheet(
                """
                QTableWidget{
                    background-color: transparent;
                }

                QHeaderView::section{
                    background-color: $primary-blue
                }
                """.replace("$primary-blue", self.active_colors['primary-blue'])
            )

    def modify_style(self, old_style: str):
        old_style = old_style.replace("$primary-blue", self.active_colors['primary-blue'])
        old_style = old_style.replace("$secondary-blue", self.active_colors['secondary-blue'])
        old_style = old_style.replace("$warn-yellow", self.active_colors['warn-yellow'])
        old_style = old_style.replace("$danger-red", self.active_colors['danger-red'])
        return old_style
