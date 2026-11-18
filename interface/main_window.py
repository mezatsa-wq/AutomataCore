from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
    QStatusBar
)

from interface.components.sidebar import Sidebar
from interface.components.topbar import TopBar

from interface.pages.home_page import HomePage
from interface.pages.expression_page import ExpressionPage
from interface.pages.automata_page import AutomataPage
from interface.pages.simulation_page import SimulationPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AutomataCore")
        self.resize(1250, 780)
        self.setMinimumSize(950, 600)

        self.setup_ui()

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Barre latérale
        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar)

        # Zone principale
        content_container = QWidget()

        content_layout = QVBoxLayout(content_container)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Barre supérieure
        self.topbar = TopBar()
        content_layout.addWidget(self.topbar)

        # Gestion des pages
        self.pages = QStackedWidget()

        self.home_page = HomePage()
        self.expression_page = ExpressionPage()
        self.automata_page = AutomataPage()
        self.simulation_page = SimulationPage()

        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.expression_page)
        self.pages.addWidget(self.automata_page)
        self.pages.addWidget(self.simulation_page)

        content_layout.addWidget(self.pages)

        main_layout.addWidget(content_container)

        # Navigation
        self.sidebar.page_changed.connect(
            self.change_page
        )

        # Événement de demande d'analyse
        self.expression_page.analyze_requested.connect(
            self.handle_analysis_request
        )

        # Barre de statut
        status_bar = QStatusBar()
        status_bar.showMessage(
            "AutomataCore - Prêt à fonctionner"
        )
        self.setStatusBar(status_bar)

        # Page initiale
        self.change_page("home")

    def change_page(self, page_id):

        pages = {
            "home": (self.home_page, "Accueil"),
            "expression": (
                self.expression_page,
                "Analyse des expressions"
            ),
            "automata": (
                self.automata_page,
                "Visualisation des automates"
            ),
            "simulation": (
                self.simulation_page,
                "Simulation des mots"
            )
        }

        if page_id not in pages:
            return

        page, title = pages[page_id]

        self.pages.setCurrentWidget(page)
        self.topbar.set_title(title)
        self.sidebar.set_active_page(page_id)

    def handle_analysis_request(self, alphabet, expression):

        self.expression_page.result_area.setPlainText(
            "Demande reçue par l'interface.\n\n"
            f"Alphabet saisi : {alphabet}\n"
            f"Expression : {expression}\n\n"
            "L'analyseur lexical et syntaxique sera "
            "connecté dans la prochaine étape."
        )