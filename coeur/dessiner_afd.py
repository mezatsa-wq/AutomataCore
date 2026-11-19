from graphviz import Digraph
from coeur.afn_afd import afn_vers_afd
from  coeur.syntax import EPSILON

def nom_etat(etat):
    return "{"+",".join(sorted(map(str,etat)))+"}"

def dessiner_afd(afd,nom_fichier="afd"):
    dot= Digraph("AFD",format="png")
    dot.attr(rankdir="LR")
    etats={afd["initial"]} | set(afd["finaux"])

    for(source,lettre), cible in afd["transitions"].items():
        etats.add(source)
        etats.add(cible)

    for etat in etats:
        if etat in afd["finaux"]:
            dot.node(nom_etat(etat), shape="doublecircle")
        else:
            dot.node(nom_etat(etat), shape="circle")
    dot.node("debut",label="", shape="none",width="0", height="0")
    dot.edge("debut",nom_etat(afd["initial"]))

    for (source,lettre), cible in afd["transitions"].items():
        dot.edge(nom_etat(source), nom_etat(cible), label=lettre)
    dot.render(nom_fichier,cleanup=True, view=True)


if __name__=="__main__":
        afn={
            "alphabet":{"a" , "b"},
            "initial": 0,
            "finaux":{3},
            "transitions":{
                (0, EPSILON):{1},
                (0, "a"):{0,1},
                (0, "b"):{0},
                (1, "b"):{2},
                (2, "b"):{3},
           },
        }
        afd=afn_vers_afd(afn)
        dessiner_afd(afd, "afd_exemple")
