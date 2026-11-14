import pytest
#MON ENSEMBLE DE TEST POUR VALIDER LES OPERATIONS
from coeur.syntax import (
    is_operator,
    is_escapable,
    decode_escape,
)


def test_operators():
    assert is_operator("*")
    assert is_operator("|")
    assert is_operator("(")
    assert not is_operator("a")


def test_escapable_characters():
    assert is_escapable("*")
    assert is_escapable("|")
    assert is_escapable("\\")
    assert is_escapable("ε")
    assert not is_escapable("a")


def test_decode_star():
    symbol, next_position = decode_escape(r"\*", 0)

    assert symbol == "*"
    assert next_position == 2


def test_decode_pipe():
    symbol, next_position = decode_escape(r"\|", 0)

    assert symbol == "|"
    assert next_position == 2


def test_decode_backslash():
    symbol, next_position = decode_escape(r"\\", 0)

    assert symbol == "\\"
    assert next_position == 2


def test_invalid_escape():
    with pytest.raises(ValueError):#with sert a definir un contexte d'exercution et pytest.raises est un outile de la bibliotheque pytest  concu pour tester les exception. il s'attend a ce que le bloc de code situe juste en dessous leve une erreur

        decode_escape(r"\a", 0)


def test_isolated_backslash():
    with pytest.raises(ValueError):
        decode_escape("\\", 0)


def test_invalid_position():
    with pytest.raises(ValueError):
        decode_escape(r"\*", 5)