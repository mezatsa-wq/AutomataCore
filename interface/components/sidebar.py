from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
)

from interface.translations import translate


class Sidebar(QFrame):

    page_changed = Signal(str)

    def __init__(self, language="fr"):
        super().__init__()

        self.language = language
        self.buttons = {}

        self.setObjectName("sidebar")
        self.setFixedWidth(235)

        self.setup_ui()
        self.update_language(language)

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 22, 15, 18)
        layout.setSpacing(12)

        self.logo = QLabel("AutomataCore")
        self.logo.setObjectName("logoLabel")

        self.logo_description = QLabel("FINITE AUTOMATA STUDIO")
        self.logo_description.setObjectName("mutedText")

        layout.addWidget(self.logo)
        layout.addWidget(self.logo_description)

        layout.addSpacing(30)

        self.nav_label = QLabel()
        self.nav_label.setObjectName("sidebarSection")

        layout.addWidget(self.nav_label)

        self.add_navigation_button(layout, "home", "house")
        self.add_navigation_button(layout, "workbench", "workflow")
        self.add_navigation_button(layout, "settings", "settings")

        layout.addStretch()

        self.version_label = QLabel("AutomataCore • Version 1.0")
        self.version_label.setObjectName("mutedText")

        layout.addWidget(self.version_label)

    def add_navigation_button(self, layout, page_key, icon_name):

        button = QPushButton()
        button.setObjectName("navButton")
        button.setCheckable(True)
        button.setMinimumHeight(43)
        button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        button.clicked.connect(
            lambda checked=False, key=page_key:
                self.page_changed.emit(key)
        )

        self.buttons[page_key] = button
        layout.addWidget(button)

    def update_language(self, language):

        self.language = language

        self.nav_label.setText(
            "NAVIGATION" if language == "en" else "NAVIGATION"
        )

        labels = {
            "home": "home",
            "workbench": "workbench",
            "settings": "settings",
        }

        for key, translation_key in labels.items():
            self.buttons[key].setText(
                translate(translation_key, language)
            )

    def set_active_page(self, page_key):

        for key, button in self.buttons.items():
            button.setChecked(key == page_key)