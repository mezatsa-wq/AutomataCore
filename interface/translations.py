TRANSLATIONS = {
    "fr": {
        "home": "Accueil",
        "workbench": "Atelier Automates",
        "settings": "Paramètres",

        "home_title": "Bienvenue dans AutomataCore",
        "home_subtitle": "Votre environnement de construction et d'étude des automates.",

        "welcome_title": "Explorez les expressions régulières et les automates",
        "welcome_description": (
            "AutomataCore permet de vérifier des expressions régulières, "
            "de construire des automates finis non déterministes et déterministes, "
            "de visualiser leurs transitions et de reconnaître des mots."
        ),

        "features_title": "Fonctionnalités du projet",

        "feature_analysis": "Analyse lexicale et syntaxique",
        "feature_analysis_desc": "Vérification des expressions régulières et analyse de leur structure.",

        "feature_thompson": "Construction par Thompson",
        "feature_thompson_desc": "Transformation d'une expression régulière validée en AFN.",

        "feature_dfa": "Déterminisation",
        "feature_dfa_desc": "Conversion de l'AFN en automate fini déterministe.",

        "feature_visualization": "Visualisation graphique",
        "feature_visualization_desc": "Affichage des états, des transitions et des automates.",

        "feature_recognition": "Reconnaissance des mots",
        "feature_recognition_desc": "Vérification de l'appartenance d'un mot au langage reconnu.",

        "feature_trace": "Simulation détaillée",
        "feature_trace_desc": "Visualisation du parcours effectué pendant la reconnaissance.",

        "appearance": "Apparence",
        "theme": "Thème",
        "dark": "Sombre",
        "light": "Clair",
        "auto": "Automatique",

        "language": "Langue",
        "french": "Français",
        "english": "Anglais",

        "settings_description": "Personnalisez l'apparence et la langue de l'application.",
    },

    "en": {
        "home": "Home",
        "workbench": "Automata Workbench",
        "settings": "Settings",

        "home_title": "Welcome to AutomataCore",
        "home_subtitle": "Your environment for automata construction and study.",

        "welcome_title": "Explore regular expressions and automata",
        "welcome_description": (
            "AutomataCore validates regular expressions, builds "
            "nondeterministic and deterministic finite automata, "
            "visualizes their transitions and recognizes words."
        ),

        "features_title": "Project features",

        "feature_analysis": "Lexical and syntax analysis",
        "feature_analysis_desc": "Validation of regular expressions and analysis of their structure.",

        "feature_thompson": "Thompson construction",
        "feature_thompson_desc": "Transformation of a validated regular expression into an NFA.",

        "feature_dfa": "Determinization",
        "feature_dfa_desc": "Conversion of an NFA into a deterministic finite automaton.",

        "feature_visualization": "Graph visualization",
        "feature_visualization_desc": "Display of states, transitions and automata.",

        "feature_recognition": "Word recognition",
        "feature_recognition_desc": "Checking whether a word belongs to the recognized language.",

        "feature_trace": "Detailed simulation",
        "feature_trace_desc": "Display of the path followed during recognition.",

        "appearance": "Appearance",
        "theme": "Theme",
        "dark": "Dark",
        "light": "Light",
        "auto": "Automatic",

        "language": "Language",
        "french": "French",
        "english": "English",

        "settings_description": "Customize the application's appearance and language.",
    },
}


def translate(key, language="fr"):

    language_dictionary = TRANSLATIONS.get(
        language,
        TRANSLATIONS["fr"]
    )

    return language_dictionary.get(
        key,
        TRANSLATIONS["fr"].get(key, key)
    )