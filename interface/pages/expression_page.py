from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QFrame
)
from PySide6.QtCore import Signal


class ExpressionPage(QWidget):

    analyze_requested = Signal(str, str)

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(18)

        title = QLabel("Analyse d'une expression régulière")
        title.setObjectName("PageTitle")

        description = QLabel(
            "Définissez votre alphabet et saisissez "
            "une expression régulière à analyser."
        )
        description.setStyleSheet("color: #94A3B8;")

        layout.addWidget(title)
        layout.addWidget(description)

        # Carte de saisie
        card = QFrame()
        card.setObjectName("ContentCard")

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(22, 22, 22, 22)
        card_layout.setSpacing(12)

        alphabet_label = QLabel("ALPHABET")

        self.alphabet_input = QLineEdit()
        self.alphabet_input.setPlaceholderText(
            "Exemple : a, b, c"
        )

        expression_label = QLabel("EXPRESSION REGULIERE")

        self.expression_input = QLineEdit()
        self.expression_input.setPlaceholderText(
            "Exemple : (a|b)*abb"
        )

        self.analyze_button = QPushButton(
            "Analyser l'expression"
        )
        self.analyze_button.setObjectName("PrimaryButton")

        self.analyze_button.clicked.connect(
            self.analyze_expression
        )

        card_layout.addWidget(alphabet_label)
        card_layout.addWidget(self.alphabet_input)
        card_layout.addSpacing(8)

        card_layout.addWidget(expression_label)
        card_layout.addWidget(self.expression_input)
        card_layout.addSpacing(12)

        card_layout.addWidget(self.analyze_button)

        layout.addWidget(card)

        result_title = QLabel("Résultat de l'analyse")

        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.result_area.setPlaceholderText(
            "Les résultats de l'analyse apparaîtront ici..."
        )

        layout.addWidget(result_title)
        layout.addWidget(self.result_area)

    def analyze_expression(self):

        alphabet = self.alphabet_input.text().strip()
        expression = self.expression_input.text().strip()

        if not alphabet or not expression:
            self.result_area.setPlainText(
                "Veuillez renseigner l'alphabet "
                "et l'expression régulière."
            )
            return

        self.analyze_requested.emit(alphabet, expression)