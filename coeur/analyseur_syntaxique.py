from coeur.tokens import Token

from coeur.arbre_syntaxique import (
    Symbol,
    Epsilon,
    Union,
    Concat,
    Star,
    Plus,
    Optional,
)

from coeur.arbre_syntaxique import CharacterClass


class Parser:
    """
    cette analyseur Reçoit une liste de tokens et construit un AST.
    """

    def __init__(self, tokens):

        self.tokens = tokens
        self.position = 0

    def _current(self):
        """Retourne le token courant. retourne le tokens courant pris dans laliste des tokens """

        if self.position < len(self.tokens):
            return self.tokens[self.position]

        return None # si il ya pas de tokens

    def _advance(self):
        """Consomme le token courant. represente le token courant et avance vers le prochain tokens"""

        token = self._current()

        if token is not None:
            self.position += 1

        return token # retourne none si le token courant est vite

    def _error(self, message):
        """Déclenche une erreur avec la position concernée."""

        token = self._current()

        if token is not None:
            position = token.position
        elif self.tokens:
            position = self.tokens[-1].position + len(
                self.tokens[-1].value
            )
        else:
            position = 0

        raise ValueError(
            f"Erreur syntaxique à la position {position} : {message}"
        )

    def _starts_atom(self):
        """Indique si le token courant peut commencer un atome."""

        token = self._current()

        return (
            token is not None
            and token.kind in {
                "SYMBOL",
                "EPSILON",
                "LEFT_PAREN",
            }
        )

    def parse(self):
        """Point d'entrée de l'analyse syntaxique."""

        if not self.tokens:
            raise ValueError(
                "L'expression régulière ne peut pas être vide."
            )

        tree = self._parse_union()

        if self._current() is not None:
            self._error(
                f"Token inattendu {self._current().value!r}."
            )

        return tree

    def _parse_union(self):
        """
        Analyse les unions.

        Exemple : a|b|c
        """

        node = self._parse_concat()

        while (
            self._current() is not None
            and self._current().kind == "UNION"
        ):

            self._advance()
           # ci dessous on verifier le caractere qui suit
            if not self._starts_atom():
                self._error(
                    "Une expression est attendue après '|'."
                )

            right = self._parse_concat()

            node = Union(node, right)

        return node

    def _parse_concat(self):
        """
        Analyse les concaténations explicites ou implicites.

        Exemples : ab, a.b, a(b|c)
        """

        node = self._parse_repetition()

        while self._current() is not None:

            token = self._current()

            # Concaténation explicite avec le point.
            if token.kind == "CONCAT":

                self._advance()
                # si ce qui suit c'est encore un symbole
                if not self._starts_atom():
                    self._error(
                        "Une expression est attendue après '.'."
                    )

                right = self._parse_repetition()
                node = Concat(node, right)

            # Concaténation implicite.
            elif self._starts_atom():

                right = self._parse_repetition()
                node = Concat(node, right)

            else:
                break

        return node

    def _parse_repetition(self):
        """
        Analyse les opérateurs *, + et ?.
        """

        node = self._parse_atom()

        token = self._current()

        if token is not None:

            if token.kind == "STAR":
                self._advance()
                node = Star(node)

            elif token.kind == "PLUS":
                self._advance()
                node = Plus(node)

            elif token.kind == "OPTIONAL":
                self._advance()
                node = Optional(node)

        # On refuse les répétitions successives comme a**.
        token = self._current()

        if token is not None and token.kind in {
            "STAR",
            "PLUS",
            "OPTIONAL",
        }:
            self._error(
                "Plusieurs opérateurs de répétition "
                "successifs ne sont pas autorisés."
            )

        return node

    def _parse_atom(self):
        """
        Analyser un symbole, epsilon ou un groupe parenthésé.
        """

        token = self._current()
        if token.kind == "CHARACTER_CLASS":
            self._advance()
            return CharacterClass(
                frozenset(token.value)
            )
        if token is None:
            self._error("Une expression est attendue.")

        # Symbole de l'alphabet.
        if token.kind == "SYMBOL":

            self._advance()
            return Symbol(token.value)

        # Mot vide.
        if token.kind == "EPSILON":

            self._advance()
            return Epsilon()

        # Expression entre parenthèses.
        if token.kind == "LEFT_PAREN":

            self._advance()

            if (
                self._current() is not None
                and self._current().kind == "RIGHT_PAREN"
            ):
                self._error(
                    "Les parenthèses ne peuvent pas être vides."
                )

            node = self._parse_union()

            if (
                self._current() is None
                or self._current().kind != "RIGHT_PAREN"
            ):
                self._error(
                    "Parenthèse fermante ')' manquante."
                )

            self._advance()

            return node

        self._error(
            f"Token inattendu {token.value!r}."
        )