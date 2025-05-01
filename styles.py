GLOBAL = """
"""

FBTN_NORMAL = """
	QPushButton{
		background-color: transparent;
		color: rgb(0, 248, 248);
		font-size: 14px;
		font-weight: bold;
		padding: 5px;
		border: 1px solid rgb(0, 248, 248);
	}

	QPushButton::hover{
		background-color: rgb(0, 179, 179);
		color: white;
	}
"""

FBTN_WARN = """
	QPushButton{
		background-color: transparent;
		color: #e6aa07;
		font-size: 14px;
		font-weight: bold;
		padding: 5px;
		border: 1px solid #e6aa07;
	}

	QPushButton::hover{
		background-color: #dfa507;
		color: white;
	}
"""

FBTN_DANGER = """
	QPushButton{
		background-color: transparent;
		color: white;
		font-size: 14px;
		font-weight: bold;
		padding: 5px;
		border: 1px solid red;
	}

	QPushButton::hover{
		background-color: #cc0000;
		color: white;
	}
"""

FTEXT_INPUT = """
    QLineEdit{
        color: white;
        font-weight: bold;
        padding-right: 10px;
        padding-left: 10px;
        font-size: 14px;
        background-color: rgb(0, 51, 51);
		border: 1px solid rgb(0, 248, 248);
    }
"""

FPROG_BAR = """
    QProgressBar{
        background-color: rgb(0, 51, 51);
		border: 1px solid rgb(0, 248, 248);
    }

    QProgressBar::chunk {
        background: rgb(0, 248, 248);
        width: 10px; /* Block width */
        margin: 0.5px; /* Space between blocks */
    }
"""

FWINDOW = """
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&display=swap');
    QMainWindow{
        background: black;
        border: 1px solid rgb(0, 248, 248);
        font-family: "Rajhdhani";
    }
"""

TITLE_BAR = """
    QFrame{
        background-color: rgb(0, 51, 51);
        border: 1px solid rgb(0, 248, 248);
    }
"""

TITLE_TEXT = """
    QLabel{
        color: #e0e0e0;
        font-family: "Rajdhani", sans-serif;
        font-weight: bold;
        font-size: 16px;
        border: none;
    }
"""

FSLIDER = """
    QSlider::groove:vertical {
        background: red;
        position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */
        left: 4px; right: 4px;
    }

    QSlider::handle:vertical {
        height: 30px;
        border-radius: 15px;
        background: cyan;
        margin: 0-4px;
    }

    QSlider::add-page:vertical {
        background: rgb(0,186, 186);
    }

    QSlider::sub-page:vertical {
        background: rgb(0, 51, 51);
    }
"""

FTAB = """
    QTabWidget{
        background-color: transparent;
        color: white;
        border: 1px solid cyan;
    }

    QTabBar::tab{
        color: white;
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 15px;
        padding-right: 15px;
        border: 1px solid rgb(0, 186, 186);
    }

    QTabBar::tab::hover{
        background-color: rgb(0, 186, 186);
    }

    QTabBar::tab::selected{
        background-color: rgb(0, 186, 186);
    }

    QTabWidget::pane{
        background-color: rgb(0, 186, 186);
    }
"""
