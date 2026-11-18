def afn_vers_afd(afn):
    initial=frozenset({afn["initial"]})
    transitions={}
    finaux=set()
    vus={initial}
    a_traiter=[initial]
    while a_traiter:
        courant=a_traiter.pop()
        if courant & afn["finaux"]:
            finaux.add(courant)
        for lettre in afn["alphabet"]:
            suivant=set()
            for etat in courant:
                suivant=suivant.union(afn["transitions"].get((etat,lettre),set()))
            if not suivant:
                continue
            suivant=frozenset(suivant)
            transitions[(courant, lettre)]=suivant
            if suivant not in vus:
                vus.add(suivant)
                a_traiter.append(suivant)
    return{"alphabet":afn["alphabet"],"initial":initial,"finaux":finaux,"transitions":transitions}