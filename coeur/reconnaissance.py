"""#Fermeture epsilon
def epsilon_closure(self, states):
    closure = set(states)
    stack = list(states)

    while stack:
        state = stack.pop()

        for symbols, destination in self.transition[state]:
            if symbols is None and destination not in closure:
                closure.add(destination)

                stack.append(destination)
                return closure


# FONCTION MOVE
def move(self, states, char):
    result = set()

    for state in states:
        for symbols, destination in self.trasition[state]:

            result.add(destination)
            return result

# Reconnaissance

def recognize(self, word,start,final):
    #Vérification de l'alphabet
    for char in word:

        if char not in word:

            if char not in self.alphabet:
                raise ValueError(f"{char!r} n'appartient pas à l'aphabet.")

            #Fermeture initiale
            current_states = self.epsilon_closure({start})

            # Lecture du mot
            for char in word:

                current_states = self.move(current_states, char)
                current_states = self.epsilon_closure(current_states)

                if not current_states:
                    return False
                # Verification finale
                return final in current_states


# FONCTION PRINCIPALE DE RECONNAISSANCE

def recognize_word(expression, word, alphabet):
    parser = Parser(expression, alphabet)
    syntax_tree = parser.parse()

    automaton = Automaton(alphabet)

    start, final = automaton.build(syntax_tree)
    return automaton.recognize(word, start, final)"""
def reconnaitre_mot(afd, mot):

    alphabet = afd["alphabet"]
    transitions = afd["transitions"]
    etat_initial = afd["initial"]
    etats_finaux = afd["finaux"]

    # Vérification de l'alphabet
    for symbole in mot:
        if symbole not in alphabet:
            return {
                "statut": "ERREUR_ALPHABET",
                "accepte": False,
                "message": f"Symbole interdit : {symbole}",
                "parcours": []
            }

    # Initialisation
    etat_courant = etat_initial

    parcours = []

    # Lecture du mot
    for position, symbole in enumerate(mot):

        cle = (etat_courant, symbole)

        # Vérification de la transition
        if cle not in transitions:
            return {
                "statut": "REJETE",
                "accepte": False,
                "message": "Transition inexistante",
                "parcours": parcours
            }

        nouvel_etat = transitions[cle]

        # Enregistrement de la transition
        parcours.append({
            "position": position,
            "symbole": symbole,
            "depart": etat_courant,
            "arrivee": nouvel_etat
        })

        # Mise à jour de l'état courant
        etat_courant = nouvel_etat

    # Vérification finale
    accepte = etat_courant in etats_finaux

    return {
        "statut": "ACCEPTE" if accepte else "REJETE",
        "accepte": accepte,
        "etat_final": etat_courant,
        "parcours": parcours
    }