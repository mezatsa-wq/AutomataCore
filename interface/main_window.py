from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
    QLabel,
    QApplication,
)

from interface.components.sidebar import Sidebar

from interface.pages.home_page import HomePage
from interface.pages.workbench_page import WorkbenchPage
from interface.pages.settings_page import SettingsPage

from interface.settings_manager import settings_manager
from interface.styles import get_stylesheet
from interface.translations import translate

from interface.services.automata_service import (
    automata_service,
    BackendNotConnected,
)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.language = settings_manager.get_language()
        self.theme = settings_manager.get_theme()

        self.setWindowTitle("AutomataCore")
        self.resize(1450, 920)
        self.setMinimumSize(1050, 700)

        self.setup_ui()
        self.connect_signals()

        self.apply_theme(self.theme)
        self.apply_language(self.language)

        self.change_page("home")

        self.statusBar().showMessage(
            "AutomataCore prêt."
        )

    # ==========================================
    # CRÉATION DE L'INTERFACE PRINCIPALE
    # ==========================================

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Barre latérale
        self.sidebar = Sidebar(self.language)

        main_layout.addWidget(self.sidebar)

        # Zone principale
        content_container = QWidget()

        content_layout = QVBoxLayout(content_container)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # En-tête supérieur
        self.top_header = QWidget()
        self.top_header.setObjectName("topHeader")
        self.top_header.setFixedHeight(58)

        header_layout = QHBoxLayout(self.top_header)
        header_layout.setContentsMargins(24, 8, 24, 8)

        self.header_title = QLabel("AutomataCore")
        self.header_title.setObjectName("sectionTitle")

        header_layout.addWidget(self.header_title)
        header_layout.addStretch()

        self.header_status = QLabel("Application prête")
        self.header_status.setObjectName("mutedText")

        header_layout.addWidget(self.header_status)

        content_layout.addWidget(self.top_header)

        # Pages
        self.pages = QStackedWidget()

        self.home_page = HomePage(self.language)
        self.workbench_page = WorkbenchPage()
        self.settings_page = SettingsPage()

        self.page_widgets = {
            "home": self.home_page,
            "workbench": self.workbench_page,
            "settings": self.settings_page,
        }

        for page in self.page_widgets.values():
            self.pages.addWidget(page)

        content_layout.addWidget(self.pages)

        main_layout.addWidget(content_container, 1)

    # ==========================================
    # CONNEXION DES SIGNAUX
    # ==========================================

    def connect_signals(self):

        # Navigation
        self.sidebar.page_changed.connect(
            self.change_page
        )

        # Atelier : construction
        self.workbench_page.construct_requested.connect(
            self.handle_construction
        )

        # Atelier : sélection AFN / AFD
        self.workbench_page.automaton_selected.connect(
            self.handle_automaton_selection
        )

        # Atelier : reconnaissance
        self.workbench_page.word_test_requested.connect(
            self.handle_word_recognition
        )

        # Paramètres
        self.settings_page.theme_changed.connect(
            self.apply_theme
        )

        self.settings_page.language_changed.connect(
            self.apply_language
        )

        # Détecter un changement de thème système en mode automatique.
        try:
            hints = QApplication.styleHints()
            hints.colorSchemeChanged.connect(
                self.handle_system_theme_changed
            )
        except (AttributeError, TypeError):
            pass

    # ==========================================
    # NAVIGATION
    # ==========================================

    def change_page(self, page_key):

        if page_key not in self.page_widgets:
            return

        page = self.page_widgets[page_key]

        self.pages.setCurrentWidget(page)

        self.sidebar.set_active_page(page_key)

        titles = {
            "home": translate("home", self.language),
            "workbench": translate("workbench", self.language),
            "settings": translate("settings", self.language),
        }

        self.header_title.setText(titles[page_key])

    # ==========================================
    # CONSTRUCTION DES AUTOMATES
    # ==========================================

    def handle_construction(self, alphabet, expression):

        self.header_status.setText("Construction en cours...")

        try:

            result = automata_service.construct_all(
                alphabet,
                expression
            )

            self.workbench_page.construction_succeeded()

            self.workbench_page.display_analysis(
                "Expression validée.\n"
                "Analyse terminée.\n"
                "AFN et AFD construits avec succès."
            )

            # Sélection initiale de l'AFN.
            self.handle_automaton_selection("AFN")

            self.header_status.setText(
                "Automates construits"
            )

            self.statusBar().showMessage(
                "Construction terminée avec succès."
            )

        except BackendNotConnected as error:

            self.workbench_page.construction_failed(
                str(error)
            )

            self.header_status.setText(
                "Algorithmes non connectés"
            )

            self.statusBar().showMessage(
                "Une fonction algorithmique manque."
            )

        except Exception as error:

            self.workbench_page.construction_failed(
                str(error)
            )

            self.header_status.setText(
                "Erreur de construction"
            )

            self.statusBar().showMessage(
                "La construction a échoué."
            )

    # ==========================================
    # SÉLECTION AFN / AFD
    # ==========================================

    def handle_automaton_selection(self, automaton_type):

        try:

            automaton = automata_service.select_automaton(
                automaton_type
            )

            if automaton_type == "AFN":
                result = automata_service.current_nfa
            else:
                result = automata_service.current_dfa

            # Afficher les transitions.
            self.workbench_page.display_transitions(
                result.transitions
            )

            # Afficher le dessin si disponible.
            if result.image_path:

                self.workbench_page.display_graph_image(
                    result.image_path
                )

            else:

                self.workbench_page.display_graph_message(
                    f"{automaton_type} sélectionné.\n"
                    "Le dessin sera affiché lorsque le module "
                    "de visualisation aura fourni son image."
                )

            self.header_status.setText(
                f"Automate actif : {automaton_type}"
            )

        except Exception as error:

            self.workbench_page.show_error(str(error))

    # ==========================================
    # RECONNAISSANCE DES MOTS
    # ==========================================

    def handle_word_recognition(self, word):

        try:

            result = automata_service.recognize_word(word)

            self.workbench_page.display_recognition(
                result
            )

            self.header_status.setText(
                "Reconnaissance terminée"
            )

        except BackendNotConnected as error:

            self.workbench_page.show_error(str(error))

        except Exception as error:

            self.workbench_page.show_error(str(error))

    # ==========================================
    # GESTION DU THÈME
    # ==========================================

    def apply_theme(self, theme):

        self.theme = theme

        if theme == "auto":
            effective_theme = self.get_system_theme()
        else:
            effective_theme = theme

        QApplication.instance().setStyleSheet(
            get_stylesheet(effective_theme)
        )

        self.header_status.setText(
            f"Thème : {effective_theme}"
        )

    def get_system_theme(self):

        try:

            hints = QApplication.styleHints()
            scheme = hints.colorScheme()

            if scheme == Qt.ColorScheme.Dark:
                return "dark"

            if scheme == Qt.ColorScheme.Light:
                return "light"

        except (AttributeError, TypeError):
            pass

        # Solution de secours selon la palette système.
        palette = QApplication.palette()

        if palette.color(
            palette.ColorRole.Window
        ).lightness() < 128:
            return "dark"

        return "light"

    def handle_system_theme_changed(self, scheme):

        if self.theme == "auto":
            self.apply_theme("auto")

    # ==========================================
    # GESTION DE LA LANGUE
    # ==========================================

    def apply_language(self, language):

        self.language = language

        self.sidebar.update_language(language)
        self.home_page.update_language(language)
        self.settings_page.update_language(language)

        current_page = self.pages.currentWidget()

        for key, page in self.page_widgets.items():

            if page == current_page:
                self.change_page(key)
                break