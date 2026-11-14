class Alphabet:

    def __init__(self, symbols):
        if isinstance(symbols, str):
            raise TypeError(
                "Fournissez une collection de symboles, "
                "par exemple ['a', 'b', 'c']."
            )

        try:
            symbols = tuple(symbols)
        except TypeError:
            raise TypeError(
                "L'alphabet doit être une collection iterable."
            )

        # l'alphabet ne peut pas etre vide.
        if not symbols:
            raise ValueError("L'alphabet ne peut pas être vide.")

        # Vérification de chaque symbole de l'alphabet.
        for symbol in symbols:

            if not isinstance(symbol, str):
                raise TypeError(
                    f"Le symbole {symbol!r} doit être une chaîne."
                )

            if symbol == "":
                raise ValueError(
                    "Un symbole ne peut pas être une chaîne vide."
                )

        # Vérification des doublons sur la chaine en comparant la talle des mots.
        if len(symbols) != len(set(symbols)):
            raise ValueError(
                "L'alphabet ne doit pas contenir de doublons."
            )

        # Conservation de l'ordre de déclaration des attributs.
        self._symbols = symbols

        # creation d'un ensemble pour accelere les recherches
        self._symbol_set = frozenset(symbols) #frozenset transforme le parametre recu en ensemle imumable donc pas modifiable

    @property
    def symbols(self):
        """Retourne les symboles de l'alphabet sous forme de tuples."""
        return self._symbols

    def contains(self, symbol):
        """pour Vérifie si un symbole appartient à l'alphabet ."""
        return symbol in self._symbol_set

    def validate_symbol(self, symbol):
        """
        Vérifie si un symbole appartient a l'alphabet en utilisant la fonction contains du haut
        et si il ya errreur ca va déclenche une ValueError(une exception).
        """
        if not self.contains(symbol):
            raise ValueError(
                f"Le symbole {symbol!r} n'appartient pas à l'alphabet."# !r demande a python d'afficheur la representaion de l'oject,enfin de visualiser un caractere particulier
            )

        return True

    def validate_symbols(self, symbols):
        """
        Vérifie plusieurs symboles et retoourne la liste des symoles inconnue et une liste vide au cas ou il ya pas d'erreur.
        """
        unknown_symbols = []#pour les symboles inconnues

        for symbol in symbols:
            if not self.contains(symbol):
                unknown_symbols.append(symbol)

        return unknown_symbols

    def __contains__(self, symbol):
        """Permet d'utiliser : symbol in alphabet."""
        return self.contains(symbol)

    def __iter__(self):
        """Permet de parcourir l'alphabet."""
        return iter(self._symbols)

    def __len__(self):
        """Retourne le nombre de symboles."""
        return len(self._symbols)

    def __repr__(self):
        return f"Alphabet({list(self._symbols)!r})"