import sys

from PySide6.QtWidgets import QApplication

from interface.main_window import MainWindow
from interface.styles import APP_STYLE


def main():

    app = QApplication(sys.argv)

    app.setApplicationName("AutomataCore")
    app.setStyle("Fusion")
    app.setStyleSheet(APP_STYLE)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()