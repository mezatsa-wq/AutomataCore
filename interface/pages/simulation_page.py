from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame,
    QTextEdit,
)


class SimulationPage(QWidget):

    word_test_requested = Signal(str)

    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(25, 25, 25, 25)
        self.main_layout.setSpacing(18)

        self.title = QLabel("Reconnaissance des mots")
        self.title.setObjectName("PageTitle")

        self.description = QLabel(
            "Saisissez un mot pour vérifier s'il est reconnu "
            "par l'automate sélectionné."
        )

        self.input_card = QFrame()
        self.input_card.setObjectName("ContentCard")

        card_layout = QVBoxLayout(self.input_card)

        self.word_label = QLabel("Mot à tester")

        self.word_input = QLineEdit()
        self.word_input.setPlaceholderText(
            "Exemple : abba"
        )

        self.test_button = QPushButton("Tester le mot")
        self.test_button.setObjectName("PrimaryButton")

        self.result_label = QLabel(
            "En attente d'un mot à tester."
        )

        self.result_label.setWordWrap(True)

        self.trace_output = QTextEdit()
        self.trace_output.setReadOnly(True)
        self.trace_output.setPlaceholderText(
            "Le détail du parcours des états apparaîtra ici."
        )

        card_layout.addWidget(self.word_label)
        card_layout.addWidget(self.word_input)
        card_layout.addWidget(self.test_button)
        card_layout.addWidget(self.result_label)

        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.description)
        self.main_layout.addWidget(self.input_card)

        self.main_layout.addWidget(
            QLabel("Détail de la simulation")
        )

        self.main_layout.addWidget(self.trace_output)

        self.test_button.clicked.connect(
            self.request_word_test
        )

        self.word_input.returnPressed.connect(
            self.request_word_test
        )

    def request_word_test(self):

        word = self.word_input.text()

        self.word_test_requested.emit(word)

    def display_result(self, accepted, message=""):

        if accepted:
            self.result_label.setText(
                "Mot accepté par l'automate."
                + (f"\n{message}" if message else "")
            )
        else:
            self.result_label.setText(
                "Mot rejeté par l'automate."
                + (f"\n{message}" if message else "")
            )

    def display_trace(self, trace):

        self.trace_output.setPlainText(str(trace))

    def display_error(self, message):

        self.result_label.setText(
            f"Impossible de tester le mot : {message}"
        )