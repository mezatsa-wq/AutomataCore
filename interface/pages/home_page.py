from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
)

from interface.translations import translate


class HomePage(QWidget):

    def __init__(self, language="fr"):
        super().__init__()

        self.language = language
        self.setup_ui()
        self.update_language(language)

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 25, 28, 25)
        layout.setSpacing(22)

        self.title = QLabel()
        self.title.setObjectName("pageTitle")

        self.subtitle = QLabel()
        self.subtitle.setObjectName("mutedText")

        layout.addWidget(self.title)
        layout.addWidget(self.subtitle)

        self.welcome_card = QFrame()
        self.welcome_card.setObjectName("welcomeCard")

        welcome_layout = QVBoxLayout(self.welcome_card)
        welcome_layout.setContentsMargins(25, 25, 25, 25)

        self.welcome_title = QLabel()
        self.welcome_title.setObjectName("welcomeTitle")

        self.welcome_description = QLabel()
        self.welcome_description.setObjectName("welcomeDescription")
        self.welcome_description.setWordWrap(True)

        welcome_layout.addWidget(self.welcome_title)
        welcome_layout.addWidget(self.welcome_description)

        layout.addWidget(self.welcome_card)

        self.features_title = QLabel()
        self.features_title.setObjectName("sectionTitle")

        layout.addWidget(self.features_title)

        grid = QGridLayout()
        grid.setSpacing(14)

        self.feature_cards = []

        features = [
            ("01", "feature_analysis", "feature_analysis_desc"),
            ("02", "feature_thompson", "feature_thompson_desc"),
            ("03", "feature_dfa", "feature_dfa_desc"),
            ("04", "feature_visualization", "feature_visualization_desc"),
            ("05", "feature_recognition", "feature_recognition_desc"),
            ("06", "feature_trace", "feature_trace_desc"),
        ]

        for index, (number, title_key, desc_key) in enumerate(features):

            card = QFrame()
            card.setObjectName("featureCard")

            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(18, 18, 18, 18)
            card_layout.setSpacing(8)

            number_label = QLabel(number)
            number_label.setObjectName("featureNumber")

            title_label = QLabel()
            title_label.setObjectName("featureTitle")

            desc_label = QLabel()
            desc_label.setObjectName("mutedText")
            desc_label.setWordWrap(True)

            card_layout.addWidget(number_label)
            card_layout.addWidget(title_label)
            card_layout.addWidget(desc_label)

            grid.addWidget(card, index // 2, index % 2)

            self.feature_cards.append(
                (title_label, desc_label, title_key, desc_key)
            )

        layout.addLayout(grid)
        layout.addStretch()

    def update_language(self, language):

        self.language = language

        self.title.setText(
            translate("home_title", language)
        )

        self.subtitle.setText(
            translate("home_subtitle", language)
        )

        self.welcome_title.setText(
            translate("welcome_title", language)
        )

        self.welcome_description.setText(
            translate("welcome_description", language)
        )

        self.features_title.setText(
            translate("features_title", language)
        )

        for title_label, desc_label, title_key, desc_key in self.feature_cards:

            title_label.setText(
                translate(title_key, language)
            )

            desc_label.setText(
                translate(desc_key, language)
            )