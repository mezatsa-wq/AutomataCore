from graphviz import Digraph

def afficher_afd(afd, etat_actif=None,
                 etats_visites=None,
                 transition_active=None):

    if etats_visites is None:
        etats_visites = set()

    graphe = Digraph()

    # Création des états
    for etat in afd["etats"]:

        couleur = "white"

        if etat in etats_visites:
            couleur = "yellow"

        if etat == etat_actif:
            couleur = "lightblue"

        forme = (
            "doublecircle"
            if etat in afd["finaux"]
            else "circle"
        )

        graphe.node(
            etat,
            shape=forme,
            style="filled",
            fillcolor=couleur
        )

    # Création des transitions
    for (depart, symbole), arrivee in afd["transitions"].items():

        couleur = "black"

        if transition_active == (depart, symbole, arrivee):
            couleur = "blue"

        graphe.edge(
            depart,
            arrivee,
            label=symbole,
            color=couleur
        )

    return graphe