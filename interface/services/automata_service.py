from interface.services.contracts import (
    AnalysisResult,
    AutomatonResult,
    RecognitionResult,
    ConstructionResult,
)


class BackendNotConnected(Exception):
    pass


class AutomataService:

    def __init__(self):
        # Fonctions fournies par les membres du groupe
        self.analyzer = None
        self.thompson_builder = None
        self.dfa_builder = None
        self.recognizer = None

        # Résultats conservés
        self.current_analysis = None
        self.current_nfa = None
        self.current_dfa = None
        self.current_automaton = None
        self.current_automaton_type = None

    # ==========================================
    # ENREGISTREMENT DES ALGORITHMES
    # ==========================================

    def register_analyzer(self, function):
        self.analyzer = function

    def register_thompson_builder(self, function):
        self.thompson_builder = function

    def register_dfa_builder(self, function):
        self.dfa_builder = function

    def register_recognizer(self, function):
        self.recognizer = function

    # ==========================================
    # ÉTAT DES CONNEXIONS
    # ==========================================

    def check_connections(self):
        missing = []

        if self.analyzer is None:
            missing.append("Analyseur")

        if self.thompson_builder is None:
            missing.append("Construction Thompson")

        if self.dfa_builder is None:
            missing.append("Déterminisation")

        if self.recognizer is None:
            missing.append("Reconnaissance")

        return missing

    # ==========================================
    # CONSTRUCTION DES AUTOMATES
    # ==========================================

    def construct_all(self, alphabet, expression):

        required = {
            "analyzer": self.analyzer,
            "thompson_builder": self.thompson_builder,
            "dfa_builder": self.dfa_builder,
        }

        for name, function in required.items():
            if function is None:
                raise BackendNotConnected(
                    f"La fonction {name} n'est pas connectée."
                )

        # Effacer les anciens résultats
        self.current_analysis = None
        self.current_nfa = None
        self.current_dfa = None
        self.current_automaton = None
        self.current_automaton_type = None

        # 1. Vérifier l'expression régulière
        analysis = self.analyzer(alphabet, expression)

        if not isinstance(analysis, AnalysisResult):
            raise TypeError(
                "L'analyseur doit retourner AnalysisResult."
            )

        if not analysis.valid:
            raise ValueError(
                analysis.message or "Expression régulière invalide."
            )

        self.current_analysis = analysis

        # 2. Construire l'AFN à partir de l'expression
        nfa = self.thompson_builder(alphabet, expression)

        if not isinstance(nfa, AutomatonResult):
            raise TypeError(
                "Thompson doit retourner AutomatonResult."
            )

        self.current_nfa = nfa

        # 3. Construire l'AFD à partir de l'AFN
        dfa = self.dfa_builder(nfa.automaton)

        if not isinstance(dfa, AutomatonResult):
            raise TypeError(
                "Le constructeur AFD doit retourner AutomatonResult."
            )

        self.current_dfa = dfa

        return ConstructionResult(
            analysis=analysis,
            nfa=nfa,
            dfa=dfa,
        )

    # ==========================================
    # CHOISIR L'AUTOMATE
    # ==========================================

    def select_automaton(self, automaton_type):

        if automaton_type == "AFN":

            if self.current_nfa is None:
                raise ValueError("AFN non construit.")

            self.current_automaton = self.current_nfa.automaton

        elif automaton_type == "AFD":

            if self.current_dfa is None:
                raise ValueError("AFD non construit.")

            self.current_automaton = self.current_dfa.automaton

        else:
            raise ValueError("Type d'automate inconnu.")

        self.current_automaton_type = automaton_type

        return self.current_automaton

    # ==========================================
    # RECONNAISSANCE D'UN MOT
    # ==========================================

    def recognize_word(self, word):

        if self.current_automaton is None:
            raise ValueError(
                "Construisez et sélectionnez d'abord un automate."
            )

        if self.recognizer is None:
            raise BackendNotConnected(
                "La reconnaissance n'est pas encore connectée."
            )

        result = self.recognizer(
            self.current_automaton,
            word
        )

        if not isinstance(result, RecognitionResult):
            raise TypeError(
                "La reconnaissance doit retourner RecognitionResult."
            )

        return result


automata_service = AutomataService()