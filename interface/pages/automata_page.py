from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QFrame,
    QTabWidget,
    QTextEdit,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)


class AutomataPage(QWidget):

    def __init__(self):
        super().__init__()

        self.current_pixmap = None

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(25, 25, 25, 25)
        self.main_layout.setSpacing(15)

        self.title = QLabel("Construction et visualisation")
        self.title.setObjectName("PageTitle")

        self.description = QLabel(
            "Visualisez les automates construits à partir "
            "de votre expression régulière."
        )

        # Sélection du type d'automate
        selector_layout = QHBoxLayout()

        self.automaton_selector = QComboBox()
        self.automaton_selector.addItem(
            "AFN - Thompson",
            "nfa"
        )
        self.automaton_selector.addItem(
            "AFD - Déterminisation",
            "dfa"
        )

        selector_layout.addWidget(
            QLabel("Type d'automate :")
        )
        selector_layout.addWidget(
            self.automaton_selector
        )
        selector_layout.addStretch()

        # Zone de résultats
        self.tabs = QTabWidget()

        # Onglet dessin
        self.graph_frame = QFrame()
        self.graph_frame.setObjectName("ContentCard")

        graph_layout = QVBoxLayout(self.graph_frame)

        self.graph_label = QLabel(
            "Le dessin de l'automate apparaîtra ici."
        )

        self.graph_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.graph_label.setMinimumHeight(350)
        self.graph_label.setWordWrap(True)

        graph_layout.addWidget(self.graph_label)

        self.tabs.addTab(
            self.graph_frame,
            "Automate"
        )

        # Onglet arbre syntaxique
        self.ast_output = QTextEdit()
        self.ast_output.setReadOnly(True)
        self.ast_output.setPlaceholderText(
            "L'arbre syntaxique apparaîtra ici."
        )

        self.tabs.addTab(
            self.ast_output,
            "Arbre syntaxique"
        )

        # Onglet table de transitions
        self.transition_table = QTableWidget()
        self.transition_table.setColumnCount(3)

        self.transition_table.setHorizontalHeaderLabels([
            "État de départ",
            "Symbole",
            "État d'arrivée",
        ])

        self.transition_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.tabs.addTab(
            self.transition_table,
            "Transitions"
        )

        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.description)
        self.main_layout.addLayout(selector_layout)
        self.main_layout.addWidget(self.tabs)

    # ===================================
    # AFFICHER UNE IMAGE GRAPHVIZ
    # ===================================

    def display_automaton_image(self, image_path):

        path = Path(image_path)

        if not path.exists():
            self.graph_label.setPixmap(QPixmap())
            self.graph_label.setText(
                f"Image introuvable : {path}"
            )
            return

        pixmap = QPixmap(str(path))

        if pixmap.isNull():
            self.graph_label.setText(
                "Impossible de charger cette image."
            )
            return

        self.current_pixmap = pixmap
        self.update_graph_size()

    def update_graph_size(self):

        if self.current_pixmap is None:
            return

        scaled = self.current_pixmap.scaled(
            self.graph_label.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.graph_label.setText("")
        self.graph_label.setPixmap(scaled)

    def resizeEvent(self, event):

        super().resizeEvent(event)
        self.update_graph_size()

    # ===================================
    # AFFICHER L'ARBRE SYNTAXIQUE
    # ===================================

    def display_ast(self, ast_text):

        self.ast_output.setPlainText(str(ast_text))
        self.tabs.setCurrentIndex(1)

    # ===================================
    # AFFICHER LES TRANSITIONS
    # ===================================

    def display_transitions(self, transitions):

        self.transition_table.setRowCount(0)

        for transition in transitions:

            row = self.transition_table.rowCount()
            self.transition_table.insertRow(row)

            values = [
                transition["source"],
                transition["symbol"],
                transition["destination"],
            ]

            for column, value in enumerate(values):

                item = QTableWidgetItem(str(value))

                self.transition_table.setItem(
                    row,
                    column,
                    item
                )

        self.tabs.setCurrentIndex(2)

    # ===================================
    # INFORMATIONS SUR L'AUTOMATE
    # ===================================

    def show_graph_message(self, message):

        self.current_pixmap = None
        self.graph_label.setPixmap(QPixmap())
        self.graph_label.setText(message)