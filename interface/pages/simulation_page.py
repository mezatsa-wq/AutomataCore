from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QFrame
)


class SimulationPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(18)

        title = QLabel("Simulation des mots")
        title.setObjectName("PageTitle")

        description = QLabel(
            "Testez un mot pour déterminer s'il est reconnu "
            "par l'automate construit."
        )
        description.setStyleSheet("color: #94A3B8;")

        layout.addWidget(title)
        layout.addWidget(description)

        card = QFrame()
        card.setObjectName("ContentCard")

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(22, 22, 22, 22)

        word_label = QLabel("MOT À TESTER")

        self.word_input = QLineEdit()
        self.word_input.setPlaceholderText(
            "Exemple : abb"
        )

        self.test_button = QPushButton("Tester le mot")
        self.test_button.setObjectName("PrimaryButton")

        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.result_area.setPlaceholderText(
            "Le résultat de la simulation apparaîtra ici."
        )

        card_layout.addWidget(word_label)
        card_layout.addWidget(self.word_input)
        card_layout.addWidget(self.test_button)
        card_layout.addWidget(self.result_area)

        layout.addWidget(card)
        layout.addStretch()