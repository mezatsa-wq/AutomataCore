from PySide6.QtCore import QSettings


class SettingsManager:

    def __init__(self):

        self.settings = QSettings(
            "AutomataCore",
            "Application"
        )

    def get_theme(self):

        return self.settings.value(
            "theme",
            "auto",
            type=str
        )

    def set_theme(self, theme):

        self.settings.setValue("theme", theme)

    def get_language(self):

        return self.settings.value(
            "language",
            "fr",
            type=str
        )

    def set_language(self, language):

        self.settings.setValue("language", language)


settings_manager = SettingsManager()