from coeur.alphabet  import Alphabet
from coeur.tokens import Token

from coeur.syntax  import (
    UNION,
    CONCAT,
    STAR,
    PLUS,
    OPTIONAL,
    LEFT_PAREN,
    RIGHT_PAREN,
    LEFT_BRACKET,
    RIGH_BRACKET,
    TIRET,
    EPSILON,
    decode_escape,
)


class Lexer:
    """
    Analyseur lexical des expressions régulières.
    """

    def __init__(self, expression, alphabet):

        if not isinstance(expression, str):
            raise TypeError(
                "L'expression doit être une chaîne."
            )

        if not isinstance(alphabet, Alphabet):
            raise TypeError(
                "L'alphabet doit être un objet Alphabet."
            )

        self.expression = expression
        self.alphabet = alphabet
        self.position = 0
        self.tokens = []

    def _add_symbol(self, symbol, position):

        if not self.alphabet.contains(symbol):
            raise ValueError(
                f"Symbole inconnu {symbol!r} "
                f"à la position {position}."
            )

        self.tokens.append(
            Token("SYMBOL", symbol, position)
        )

    def _read_braced_symbol(self):
        # ici start c'est la position de depuis du symbole entre accolade et closing_position c'est la position de fin
        start = self.position

        closing_position = self.expression.find(
            "}",
            start + 1
        )

        if closing_position == -1:
            raise ValueError(
                f"Accolade fermante manquante "
                f"à la position {start}."
            )

        symbol = self.expression[start + 1:closing_position]

        if not symbol:
            raise ValueError(
                f"Symbole vide à la position {start}."
            )

        if "{" in symbol:
            raise ValueError(
                f"Accolade ouvrante inattendue à la position {start}."
            )

        self._add_symbol(symbol, start)

        self.position = closing_position + 1#position fermante de la l'expression sur les accolades

    def _read_character_class(self):
        """
        Analyse une classe de caractères.
          pour les symbole entre les brackets
        Exemples :
            [abc]
            [a-b]
            [a-z]

        Produit un token CHARACTER_CLASS
        contenant les symboles reconnus.
        """

        start = self.position

        self.position += 1

        characters = []

        while self.position < len(self.expression):

            character = self.expression[self.position]

            if character == RIGH_BRACKET:
                break

            if character.isspace():
                raise ValueError(
                    "Les espaces ne sont pas autorisés "
                    "dans une classe de caractères."
                )

            if character in {"[", "{", "}"}:
                raise ValueError(
                    f"Caractère inattendu {character!r} "
                    f"dans la classe à la position {self.position}."
                )

            if character == "\\":
                symbol, next_position = decode_escape(
                    self.expression,
                    self.position
                )

                characters.append((symbol, True))
                self.position = next_position

            else:
                characters.append((character, False))
                self.position += 1

        if self.position >= len(self.expression):
            raise ValueError(
                f"Crochet fermant ']' manquant à la position {start}."
            )

        if not characters:
            raise ValueError(
                f"La classe de caractères à la position {start} "
                "ne peut pas être vide."
            )

        self.position += 1

        result = []
        index = 0

        while index < len(characters):

            current, escaped = characters[index]

            # Un tiret non échappé indique un intervalle.
            if current == "-" and not escaped:
                raise ValueError(
                    f"Intervalle sans symbole de départ "
                    f"à la position {start}."
                )

            # Vérifier si le prochain élément est un tiret.
            if (
                index + 1 < len(characters)
                and characters[index + 1] == ("-", False)
            ):

                if index + 2 >= len(characters):
                    raise ValueError(
                        "Un intervalle doit avoir une borne finale."
                    )

                end, end_escaped = characters[index + 2]

                if escaped or end_escaped:
                    raise ValueError(
                        "Les bornes d'un intervalle "
                        "doivent être des caractères simples."
                    )

                if len(current) != 1 or len(end) != 1:
                    raise ValueError(
                        "Les bornes d'un intervalle "
                        "doivent être des caractères simples."
                    )

                if ord(current) > ord(end):
                    raise ValueError(
                        f"Intervalle incorrect : {current}-{end}."
                    )

                expanded = [
                    chr(code)
                    for code in range(ord(current), ord(end) + 1)
                ]

                result.extend(expanded)

                index += 3

            else:
                result.append(current)
                index += 1

        # Supprimer les doublons en conservant l'ordre.
        result = list(dict.fromkeys(result))

        # Vérifier que tous les symboles sont dans l'alphabet.
        unknown = self.alphabet.validate_symbols(result)

        if unknown:
            raise ValueError(
                f"Les symboles {unknown!r} générés par la classe "
                "n'appartiennent pas à l'alphabet."
            )

        self.tokens.append(
            Token(
                "CHARACTER_CLASS",
                tuple(result),
                start
            )
        )

    def tokenize(self):

        self.position = 0
        self.tokens = []

        operator_tokens = {
            UNION: "UNION",
            CONCAT: "CONCAT",
            STAR: "STAR",
            PLUS: "PLUS",
            OPTIONAL: "OPTIONAL",
            LEFT_PAREN: "LEFT_PAREN",
            RIGHT_PAREN: "RIGHT_PAREN",
        }

        while self.position < len(self.expression):

            character = self.expression[self.position]

            if character.isspace():
                self.position += 1
                continue

            if character == "\\":
                start = self.position

                symbol, next_position = decode_escape(
                    self.expression,
                    self.position
                )

                self._add_symbol(symbol, start)
                self.position = next_position
                continue

            if character == "{":
                self._read_braced_symbol()
                continue

            if character == LEFT_BRACKET:
                self._read_character_class()
                continue

            if character == RIGH_BRACKET:
                raise ValueError(
                    f"Crochet fermant inattendu "
                    f"à la position {self.position}."
                )

            if character == EPSILON:
                self.tokens.append(
                    Token("EPSILON", EPSILON, self.position)
                )

                self.position += 1
                continue

            if character in operator_tokens:
                self.tokens.append(
                    Token(
                        operator_tokens[character],
                        character,
                        self.position
                    )
                )

                self.position += 1
                continue

            if character == "}":
                raise ValueError(
                    f"Accolade fermante inattendue "
                    f"à la position {self.position}."
                )

            self._add_symbol(character, self.position)
            self.position += 1

        return self.tokens