from coeur.afn_afd import afn_vers_afd
from coeur.syntax import EPSILON
import pytest

def test_finit_par_ab():
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
    assert len(afd["finaux"])==1
    assert frozenset({"q0","q2"}) in afd["finaux"]


def test_avec_epsilon():
    afn = {
        "alphabet":{"a"},
        "initial":"q0",
        "finaux":{"q2"},
        "transitions":{
            ("q0",EPSILON):{"q1"},
            ("q1","a"):{"q2"},
      },
    }
    afd=afn_vers_afd(afn)
    assert afd["initial"]==frozenset({"q0","q1"})
    assert frozenset({"q2"}) in afd["finaux"]
