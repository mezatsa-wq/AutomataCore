from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy
)
from PySide6.QtCore import Signal, Qt


class Sidebar(QFrame):

    page_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("Sidebar")
        self.setFixedWidth(235)

        self.buttons = {}

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 25, 15, 20)
        layout.setSpacing(10)

        # Logo et nom de l'application
        title = QLabel("◈  AutomataCore")
        title.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: white;"
        )

        subtitle = QLabel("Regular Expressions & Automata")
        subtitle.setStyleSheet(
            "color: #8996AD; font-size: 10px;"
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(35)

        section = QLabel("WORKSPACE")
        section.setStyleSheet(
            "color: #718096; font-size: 10px; font-weight: bold;"
        )

        layout.addWidget(section)

        # Pages de navigation
        self.add_navigation_button(
            layout, "⌂  Accueil", "home"
        )

        self.add_navigation_button(
            layout, "⌘  Expressions", "expression"
        )

        self.add_navigation_button(
            layout, "◎  Automates", "automata"
        )

        self.add_navigation_button(
            layout, "▷  Simulation", "simulation"
        )

        layout.addStretch()

        footer = QLabel("AUTOMATACORE  •  VERSION 1.0")
        footer.setStyleSheet(
            "color: #64748B; font-size: 9px;"
        )

        layout.addWidget(footer)

    def add_navigation_button(self, layout, text, page_id):

        button = QPushButton(text)

        button.setObjectName("NavButton")
        button.setCheckable(True)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        button.clicked.connect(
            lambda checked=False, page=page_id:
            self.page_changed.emit(page)
        )

        self.buttons[page_id] = button
        layout.addWidget(button)

    def set_active_page(self, page_id):

        for name, button in self.buttons.items():
            button.setChecked(name == page_id)