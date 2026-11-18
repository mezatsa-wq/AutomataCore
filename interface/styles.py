APP_STYLE = """
QWidget {
    background-color: #0B1020;
    color: #E5E7EB;
    font-family: "Segoe UI";
    font-size: 13px;
}

QMainWindow {
    background-color: #0B1020;
}

QFrame#Sidebar {
    background-color: #080D19;
    border-right: 1px solid #202A40;
}

QFrame#TopBar {
    background-color: #0B1020;
    border-bottom: 1px solid #202A40;
}

QLabel#AppTitle {
    color: #FFFFFF;
    font-size: 19px;
    font-weight: bold;
}

QLabel#PageTitle {
    color: #FFFFFF;
    font-size: 23px;
    font-weight: bold;
}

QLabel#MutedText {
    color: #94A3B8;
}

QPushButton {
    background-color: #182238;
    color: #E5E7EB;
    border: 1px solid #293650;
    border-radius: 8px;
    padding: 10px 14px;
}

QPushButton:hover {
    background-color: #273653;
    border-color: #7C5CFF;
}

QPushButton:pressed {
    background-color: #35256A;
}

QPushButton#PrimaryButton {
    background-color: #7047EB;
    color: white;
    border: none;
    font-weight: bold;
}

QPushButton#PrimaryButton:hover {
    background-color: #825FF3;
}

QPushButton#NavButton {
    background-color: transparent;
    border: none;
    color: #AAB6CA;
    text-align: left;
    padding: 12px;
}

QPushButton#NavButton:hover {
    background-color: #182238;
    color: white;
}

QPushButton#NavButton:checked {
    background-color: #29204A;
    color: #BBA7FF;
    border-left: 3px solid #8B6CFF;
}

QLineEdit, QTextEdit {
    background-color: #111B2E;
    border: 1px solid #293650;
    border-radius: 8px;
    padding: 10px;
    color: #FFFFFF;
    selection-background-color: #7047EB;
}

QLineEdit:focus, QTextEdit:focus {
    border: 1px solid #8B6CFF;
}

QTextEdit {
    padding: 12px;
}

QScrollArea {
    border: none;
}

QFrame#ContentCard {
    background-color: #111B2E;
    border: 1px solid #202F49;
    border-radius: 12px;
}

QLabel#StatusLabel {
    color: #A78BFA;
    background-color: #211A3B;
    border-radius: 7px;
    padding: 8px;
}

QStatusBar {
    background-color: #080D19;
    color: #94A3B8;
    border-top: 1px solid #202A40;
}
"""