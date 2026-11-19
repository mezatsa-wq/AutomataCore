from coeur.syntax import EPSILON
def epsilon_fermeture(etats,transitions):
    resultat=set(etats)
    a_traiter=list(etats)
    while a_traiter:
        etat=a_traiter.pop()
        for voisin in transitions.get((etat,EPSILON),set()):
            if voisin not in resultat:
                resultat.add(voisin)
                a_traiter.append(voisin)
    return frozenset(resultat)

def afn_vers_afd(afn):
    trans_afn=afn["transitions"]
    initial=epsilon_fermeture({afn["initial"]},trans_afn)
    transitions={}
    finaux=set()
    vus={initial}
    a_traiter=[initial]
    while a_traiter:
        courant=a_traiter.pop()
        if courant & afn["finaux"]:
            finaux.add(courant)
        for lettre in afn["alphabet"]:
            if lettre==EPSILON:
                continue
            suivant=set()
            for etat in courant:
                suivant=suivant.union(trans_afn.get((etat,lettre),set()))
            if not suivant:
                continue
            suivant=epsilon_fermeture(suivant,trans_afn)
            transitions[(courant, lettre)]=suivant
            if suivant not in vus:
                vus.add(suivant)
                a_traiter.append(suivant)
    return{"alphabet":afn["alphabet"] -{EPSILON},"initial":initial,"finaux":finaux,"transitions":transitions}