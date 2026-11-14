"""
Définitions syntaxiques utilisées par AutomataCore.

Ce module ne construit pas encore les automates.
Il définit les opérateurs et les règles d'échappement.
"""

# Opérateurs de notre langage.
UNION = "|"
CONCAT = "."
STAR = "*"
PLUS = "+"
OPTIONAL = "?"
LEFT_PAREN = "("
RIGHT_PAREN = ")"

# Symbole représentant le mot vide.
EPSILON = "ε"

# Ensemble des caractères réservés.
OPERATORS = frozenset({
    UNION,
    CONCAT,
    STAR,
    PLUS,
    OPTIONAL,
    LEFT_PAREN,
    RIGHT_PAREN,
})

# Caractères spéciaux pouvant être échappés et mis avant slash \.
# Exemple : \* représente le symbole ordinaire "*".
ESCAPABLE_SYMBOLS = frozenset({
    "|",
    ".",
    "*",
    "+",
    "?",
    "(",
    ")",
    "{",
    "}",
    "\\",
    "ε",
})


def is_operator(character):
    """pour savoir si un caracteres fait partie des operateurs"""
    return character in OPERATORS


def is_escapable(character):
    """Indique si un caracteres fait partie des escapables declarer en haut."""
    return character in ESCAPABLE_SYMBOLS


def decode_escape(expression, position):
    """
   premier prametre est l'expression et le second la possition du caractere special a echapper
    """

    if position >= len(expression):
        raise ValueError(
            "Position invalide dans l'expression."
        )

    if expression[position] != "\\":
        raise ValueError(
            "La position indiquée ne contient pas d'antislash."
        )

    if position + 1 >= len(expression):
        raise ValueError(
            "Antislash isolé : aucun caractère à échapper."
        )

    character = expression[position + 1]

    if not is_escapable(character):
        raise ValueError(
            f"Le caractère {character!r} ne peut pas être échappé."
        )

    return character, position + 2