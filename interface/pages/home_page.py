from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame
)


class HomePage(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def create_card(self, title, description):

        card = QFrame()
        card.setObjectName("ContentCard")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        title_label = QLabel(title)
        title_label.setStyleSheet(
            "font-size: 17px; font-weight: bold; color: white;"
        )

        description_label = QLabel(description)
        description_label.setWordWrap(True)
        description_label.setStyleSheet(
            "color: #94A3B8;"
        )

        layout.addWidget(title_label)
        layout.addWidget(description_label)

        return card

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        welcome = QLabel("Bienvenue dans AutomataCore")
        welcome.setObjectName("PageTitle")

        description = QLabel(
            "Un environnement pour analyser les expressions "
            "régulières et construire des automates finis."
        )
        description.setWordWrap(True)
        description.setStyleSheet(
            "color: #94A3B8; font-size: 14px;"
        )

        layout.addWidget(welcome)
        layout.addWidget(description)

        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(15)

        cards_layout.addWidget(
            self.create_card(
                "Analyse lexicale",
                "Identifier les symboles et les opérateurs "
                "de vos expressions régulières."
            )
        )

        cards_layout.addWidget(
            self.create_card(
                "Analyse syntaxique",
                "Vérifier la grammaire et construire "
                "l'arbre syntaxique."
            )
        )

        cards_layout.addWidget(
            self.create_card(
                "Construction d'automates",
                "Construire les automates avec "
                "la méthode de Thompson."
            )
        )

        layout.addLayout(cards_layout)
        layout.addStretch()