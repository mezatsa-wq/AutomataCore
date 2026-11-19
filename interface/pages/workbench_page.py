from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame,
    QTabWidget,
    QTextEdit,
    QComboBox,
    QSizePolicy,
)


class WorkbenchPage(QWidget):

    # Demande de construction des automates
    construct_requested = Signal(str, str)

    # Changement d'automate à visualiser
    automaton_selected = Signal(str)

    # Demande de reconnaissance d'un mot
    word_test_requested = Signal(str)

    def __init__(self):
        super().__init__()
        self.current_graph_pixmap = None
        self.current_automaton_type = "AFN"

        self.setup_ui()
        self.connect_signals()

    # ==========================================
    # CONSTRUCTION DE L'INTERFACE
    # ==========================================

    def setup_ui(self):

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(25, 20, 25, 20)
        main_layout.setSpacing(18)

        # --------------------------------------
        # EN-TÊTE
        # --------------------------------------

        header_layout = QHBoxLayout()

        title_layout = QVBoxLayout()

        self.title_label = QLabel("Atelier Automates")
        self.title_label.setObjectName("pageTitle")

        self.subtitle_label = QLabel(
            "Construisez, visualisez et testez vos automates."
        )
        self.subtitle_label.setObjectName("mutedText")

        title_layout.addWidget(self.title_label)
        title_layout.addWidget(self.subtitle_label)

        header_layout.addLayout(title_layout)
        header_layout.addStretch()

        self.status_label = QLabel("En attente d'une expression")
        self.status_label.setObjectName("statusBadge")

        header_layout.addWidget(self.status_label)

        main_layout.addLayout(header_layout)

        # --------------------------------------
        # CARTE DES ENTRÉES
        # --------------------------------------

        input_card = QFrame()
        input_card.setObjectName("contentCard")

        input_layout = QVBoxLayout(input_card)
        input_layout.setContentsMargins(20, 18, 20, 18)
        input_layout.setSpacing(12)

        input_title = QLabel("Définir votre expression")
        input_title.setObjectName("sectionTitle")

        input_layout.addWidget(input_title)

        fields_layout = QGridLayout()
        fields_layout.setHorizontalSpacing(15)
        fields_layout.setVerticalSpacing(8)

        self.alphabet_label = QLabel("Alphabet")
        self.alphabet_input = QLineEdit()
        self.alphabet_input.setPlaceholderText(
            "Exemple : a, b, c"
        )

        self.expression_label = QLabel("Expression régulière")
        self.expression_input = QLineEdit()
        self.expression_input.setPlaceholderText(
            "Exemple : a(b|c)*"
        )

        fields_layout.addWidget(self.alphabet_label, 0, 0)
        fields_layout.addWidget(self.expression_label, 0, 1)

        fields_layout.addWidget(self.alphabet_input, 1, 0)
        fields_layout.addWidget(self.expression_input, 1, 1)

        input_layout.addLayout(fields_layout)

        self.construct_button = QPushButton(
            "Construire les automates"
        )
        self.construct_button.setObjectName("primaryButton")
        self.construct_button.setMinimumHeight(42)

        input_layout.addWidget(self.construct_button)

        main_layout.addWidget(input_card)

        # --------------------------------------
        # ZONE DES RÉSULTATS
        # --------------------------------------

        result_header = QHBoxLayout()

        self.result_title = QLabel("Résultat de la construction")
        self.result_title.setObjectName("sectionTitle")

        result_header.addWidget(self.result_title)
        result_header.addStretch()

        self.automaton_selector = QComboBox()
        self.automaton_selector.addItems(["AFN", "AFD"])
        self.automaton_selector.setEnabled(False)

        result_header.addWidget(QLabel("Automate :"))
        result_header.addWidget(self.automaton_selector)

        main_layout.addLayout(result_header)

        # --------------------------------------
        # ONGLETS DE VISUALISATION
        # --------------------------------------

        self.result_tabs = QTabWidget()
        self.result_tabs.setObjectName("resultTabs")

        # Onglet Graphe
        self.graph_tab = QWidget()
        graph_layout = QVBoxLayout(self.graph_tab)

        self.graph_message = QLabel(
            "Le dessin de l'automate apparaîtra ici après la construction."
        )
        self.graph_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.graph_message.setObjectName("graphPlaceholder")
        self.graph_message.setMinimumHeight(250)

        self.graph_message.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        graph_layout.addWidget(self.graph_message)

        # Onglet Transitions
        self.transitions_tab = QWidget()
        transitions_layout = QVBoxLayout(self.transitions_tab)

        self.transitions_output = QTextEdit()
        self.transitions_output.setReadOnly(True)
        self.transitions_output.setPlaceholderText(
            "Les transitions de l'automate apparaîtront ici."
        )

        transitions_layout.addWidget(self.transitions_output)

        # Onglet Analyse
        self.analysis_tab = QWidget()
        analysis_layout = QVBoxLayout(self.analysis_tab)

        self.analysis_output = QTextEdit()
        self.analysis_output.setReadOnly(True)
        self.analysis_output.setPlaceholderText(
            "Les informations de validation et d'analyse apparaîtront ici."
        )

        analysis_layout.addWidget(self.analysis_output)

        self.result_tabs.addTab(self.graph_tab, "Visualisation")
        self.result_tabs.addTab(self.transitions_tab, "Transitions")
        self.result_tabs.addTab(self.analysis_tab, "Analyse")

        main_layout.addWidget(self.result_tabs, 1)

        # --------------------------------------
        # ZONE DE RECONNAISSANCE
        # --------------------------------------

        simulation_card = QFrame()
        simulation_card.setObjectName("contentCard")

        simulation_layout = QVBoxLayout(simulation_card)
        simulation_layout.setContentsMargins(20, 16, 20, 16)
        simulation_layout.setSpacing(10)

        self.simulation_title = QLabel("Reconnaissance des mots")
        self.simulation_title.setObjectName("sectionTitle")

        simulation_layout.addWidget(self.simulation_title)

        word_layout = QHBoxLayout()

        self.word_input = QLineEdit()
        self.word_input.setPlaceholderText(
            "Entrez le mot à tester..."
        )
        self.word_input.setEnabled(False)

        self.test_button = QPushButton("Tester le mot")
        self.test_button.setEnabled(False)

        word_layout.addWidget(self.word_input, 1)
        word_layout.addWidget(self.test_button)

        simulation_layout.addLayout(word_layout)

        self.recognition_result = QLabel(
            "Construisez d'abord un automate pour tester un mot."
        )
        self.recognition_result.setObjectName("mutedText")

        simulation_layout.addWidget(self.recognition_result)

        self.trace_output = QTextEdit()
        self.trace_output.setReadOnly(True)
        self.trace_output.setPlaceholderText(
            "Le parcours de l'automate apparaîtra ici."
        )
        self.trace_output.setMaximumHeight(130)

        simulation_layout.addWidget(self.trace_output)

        main_layout.addWidget(simulation_card)

        # --------------------------------------
        # ZONE DES ERREURS
        # --------------------------------------

        self.error_label = QLabel("")
        self.error_label.setObjectName("errorMessage")
        self.error_label.setWordWrap(True)

        main_layout.addWidget(self.error_label)

    # ==========================================
    # CONNEXION DES SIGNAUX
    # ==========================================

    def connect_signals(self):

        self.construct_button.clicked.connect(
            self.request_construction
        )

        self.automaton_selector.currentTextChanged.connect(
            self.select_automaton
        )

        self.test_button.clicked.connect(
            self.request_word_test
        )

        self.word_input.returnPressed.connect(
            self.request_word_test
        )

    # ==========================================
    # DEMANDER LA CONSTRUCTION
    # ==========================================

    def request_construction(self):

        alphabet = self.alphabet_input.text().strip()
        expression = self.expression_input.text().strip()

        if not alphabet:
            self.show_error("Veuillez saisir un alphabet.")
            return

        if not expression:
            self.show_error(
                "Veuillez saisir une expression régulière."
            )
            return

        self.clear_results()

        self.status_label.setText("Construction en cours...")
        self.construct_button.setEnabled(False)

        self.construct_requested.emit(
            alphabet,
            expression
        )

    # ==========================================
    # SÉLECTION AFN / AFD
    # ==========================================

    def select_automaton(self, automaton_type):

        self.current_automaton_type = automaton_type

        self.automaton_selected.emit(automaton_type)

    # ==========================================
    # DEMANDER LA RECONNAISSANCE
    # ==========================================

    def request_word_test(self):

        word = self.word_input.text()

        if not word:
            self.show_error("Veuillez saisir un mot.")
            return

        self.error_label.clear()
        self.trace_output.clear()

        self.word_test_requested.emit(word)

    # ==========================================
    # AFFICHER LE RÉSULTAT DE CONSTRUCTION
    # ==========================================

    def construction_succeeded(self):

        self.status_label.setText("Automates construits")
        self.construct_button.setEnabled(True)

        self.automaton_selector.setEnabled(True)
        self.word_input.setEnabled(True)
        self.test_button.setEnabled(True)

        self.automaton_selector.setCurrentText("AFN")

    def construction_failed(self, message):

        self.status_label.setText("Échec de la construction")
        self.construct_button.setEnabled(True)

        self.automaton_selector.setEnabled(False)
        self.word_input.setEnabled(False)
        self.test_button.setEnabled(False)

        self.show_error(message)

    # ==========================================
    # AFFICHAGE DES RÉSULTATS
    # ==========================================

    def display_graph_message(self, message):

        self.graph_message.setText(message)

    def display_transitions(self, transitions):

        self.transitions_output.setPlainText(
            str(transitions)
        )

    def display_analysis(self, message):

        self.analysis_output.setPlainText(message)

    def display_recognition(self, result):

        if result.accepted:
            self.recognition_result.setText(
                "✓ Mot accepté par l'automate."
            )
        else:
            self.recognition_result.setText(
                "✗ Mot rejeté par l'automate."
            )

        self.trace_output.setPlainText(
            "\n".join(map(str, result.trace))
        )

        if result.message:
            self.trace_output.append("\n" + result.message)

    # ==========================================
    # GESTION DES ERREURS
    # ==========================================

    def show_error(self, message):

        self.error_label.setText("Erreur : " + str(message))

    def clear_results(self):

        self.error_label.clear()
        self.analysis_output.clear()
        self.transitions_output.clear()
        self.trace_output.clear()

        self.recognition_result.setText(
            "En attente de la construction..."
        )

        self.graph_message.setText(
            "Construction en cours..."
        )

        self.automaton_selector.setEnabled(False)
        self.word_input.setEnabled(False)
        self.test_button.setEnabled(False)
        self.current_graph_pixmap = None
        # ==========================================
        # AFFICHAGE DU GRAPHE GRAPHVIZ
        # ==========================================

    def display_graph_image(self, image_path):

            pixmap = QPixmap(str(image_path))

            if pixmap.isNull():
                self.show_error(
                    f"Impossible de charger l'image : {image_path}"
                )
                return

            self.current_graph_pixmap = pixmap

            self.graph_message.setText("")
            self.graph_message.setPixmap(
                pixmap.scaled(
                    self.graph_message.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            )

            self.graph_message.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

    def resizeEvent(self, event):

            super().resizeEvent(event)

            if self.current_graph_pixmap is not None:
                self.graph_message.setPixmap(
                    self.current_graph_pixmap.scaled(
                        self.graph_message.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                )