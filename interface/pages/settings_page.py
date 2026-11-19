from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QFrame,
)

from interface.settings_manager import settings_manager
from interface.translations import translate


class SettingsPage(QWidget):

    theme_changed = Signal(str)
    language_changed = Signal(str)

    def __init__(self):

        super().__init__()

        self.setup_ui()
        self.load_settings()

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 25, 28, 25)
        layout.setSpacing(20)

        self.title = QLabel()
        self.title.setObjectName("pageTitle")

        self.description = QLabel()
        self.description.setObjectName("mutedText")

        layout.addWidget(self.title)
        layout.addWidget(self.description)

        # Carte apparence
        self.appearance_card = QFrame()
        self.appearance_card.setObjectName("contentCard")

        appearance_layout = QVBoxLayout(self.appearance_card)
        appearance_layout.setContentsMargins(22, 20, 22, 20)
        appearance_layout.setSpacing(12)

        self.appearance_title = QLabel()
        self.appearance_title.setObjectName("sectionTitle")

        appearance_layout.addWidget(self.appearance_title)

        theme_row = QHBoxLayout()

        self.theme_label = QLabel()

        self.theme_combo = QComboBox()
        self.theme_combo.addItem("Sombre", "dark")
        self.theme_combo.addItem("Clair", "light")
        self.theme_combo.addItem("Automatique", "auto")

        theme_row.addWidget(self.theme_label)
        theme_row.addStretch()
        theme_row.addWidget(self.theme_combo)

        appearance_layout.addLayout(theme_row)

        layout.addWidget(self.appearance_card)

        # Carte langue
        self.language_card = QFrame()
        self.language_card.setObjectName("contentCard")

        language_layout = QVBoxLayout(self.language_card)
        language_layout.setContentsMargins(22, 20, 22, 20)
        language_layout.setSpacing(12)

        self.language_title = QLabel()
        self.language_title.setObjectName("sectionTitle")

        language_layout.addWidget(self.language_title)

        language_row = QHBoxLayout()

        self.language_label = QLabel()

        self.language_combo = QComboBox()
        self.language_combo.addItem("Français", "fr")
        self.language_combo.addItem("English", "en")

        language_row.addWidget(self.language_label)
        language_row.addStretch()
        language_row.addWidget(self.language_combo)

        language_layout.addLayout(language_row)

        layout.addWidget(self.language_card)
        layout.addStretch()

        # Signaux
        self.theme_combo.currentIndexChanged.connect(
            lambda index: self.on_theme_changed()
        )

        self.language_combo.currentIndexChanged.connect(
            lambda index: self.on_language_changed()
        )

    def load_settings(self):

        theme = settings_manager.get_theme()
        language = settings_manager.get_language()

        theme_index = self.theme_combo.findData(theme)
        language_index = self.language_combo.findData(language)

        self.theme_combo.blockSignals(True)
        self.language_combo.blockSignals(True)

        self.theme_combo.setCurrentIndex(
            theme_index if theme_index >= 0 else 2
        )

        self.language_combo.setCurrentIndex(
            language_index if language_index >= 0 else 0
        )

        self.theme_combo.blockSignals(False)
        self.language_combo.blockSignals(False)

        self.update_language(language)

    def on_theme_changed(self):

        theme = self.theme_combo.currentData()

        settings_manager.set_theme(theme)
        self.theme_changed.emit(theme)

    def on_language_changed(self):

        language = self.language_combo.currentData()

        settings_manager.set_language(language)
        self.update_language(language)
        self.language_changed.emit(language)

    def update_language(self, language):

        self.title.setText(
            translate("settings", language)
        )

        self.description.setText(
            translate("settings_description", language)
        )

        self.appearance_title.setText(
            translate("appearance", language)
        )

        self.theme_label.setText(
            translate("theme", language)
        )

        self.language_title.setText(
            translate("language", language)
        )

        self.language_label.setText(
            translate("language", language)
        )

        self.theme_combo.setItemText(
            0, translate("dark", language)
        )

        self.theme_combo.setItemText(
            1, translate("light", language)
        )

        self.theme_combo.setItemText(
            2, translate("auto", language)
        )

        self.language_combo.setItemText(
            0, translate("french", language)
        )

        self.language_combo.setItemText(
            1, translate("english", language)
        )