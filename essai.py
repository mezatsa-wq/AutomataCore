from  coeur.afn_afd import  afn_vers_afd
from coeur.syntax import EPSILON

afn = {
        "alphabet":{"a","b"},
        "initial":"q0",
        "finaux":{"q2"},
        "transitions": {
            ("q0","a"):{"q0","q1"},
            ("q0","b"):{"q0"},
            ("q1","b"):{"q2"},
         },
}

afd = afn_vers_afd(afn)
print("initial:",set(afd["initial"]))
print("Finaux:",[set(e) for e in afd["finaux"]])
for (etat,lettre),dest in afd["transitions"].items():
    print(set(etat),"--",lettre,"->",set(dest))