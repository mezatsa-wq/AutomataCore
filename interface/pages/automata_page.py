from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QComboBox
)
from PySide6.QtCore import Qt


class AutomataPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(18)

        title = QLabel("Visualisation des automates")
        title.setObjectName("PageTitle")

        description = QLabel(
            "Visualisez les automates générés à partir "
            "de votre expression régulière."
        )
        description.setStyleSheet("color: #94A3B8;")

        layout.addWidget(title)
        layout.addWidget(description)

        controls = QHBoxLayout()

        self.automata_selector = QComboBox()
        self.automata_selector.addItems([
            "AFN - Thompson",
            "AFD - Déterminisation"
        ])

        self.refresh_button = QPushButton("Actualiser")

        controls.addWidget(self.automata_selector)
        controls.addWidget(self.refresh_button)
        controls.addStretch()

        layout.addLayout(controls)

        self.graph_area = QFrame()
        self.graph_area.setObjectName("ContentCard")

        graph_layout = QVBoxLayout(self.graph_area)

        self.graph_label = QLabel(
            "L'automate sera affiché ici après sa construction."
        )

        self.graph_label.setStyleSheet(
            "color: #94A3B8; font-size: 14px;"
        )

        self.graph_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
            )


        graph_layout.addWidget(self.graph_label)

        layout.addWidget(self.graph_area, 1)