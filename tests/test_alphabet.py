import pytest

from coeur.alphabet import Alphabet


def test_create_alphabet():
    alphabet = Alphabet(["a", "b", "c"])

    assert len(alphabet) == 3
    assert alphabet.symbols == ("a", "b", "c")


def test_symbol_membership():
    alphabet = Alphabet(["a", "b", "c"])

    assert alphabet.contains("a")
    assert "b" in alphabet
    assert not alphabet.contains("d")


def test_multi_character_symbols():
    alphabet = Alphabet(["a", "bonjour", "if"])

    assert "bonjour" in alphabet
    assert "if" in alphabet


def test_special_characters_in_alphabet():
    alphabet = Alphabet(["a", "*", "|", "(", "\\"])

    assert "*" in alphabet
    assert "|" in alphabet
    assert "(" in alphabet
    assert "\\" in alphabet


def test_validate_symbol():
    alphabet = Alphabet(["a", "b"])

    assert alphabet.validate_symbol("a") is True

    with pytest.raises(ValueError):
        alphabet.validate_symbol("x")


def test_validate_multiple_symbols():
    alphabet = Alphabet(["a", "b", "c"])

    unknown = alphabet.validate_symbols(["a", "x", "c"])

    assert unknown == ["x"]


def test_empty_alphabet():
    with pytest.raises(ValueError):
        Alphabet([])


def test_duplicate_symbols():
    with pytest.raises(ValueError):
        Alphabet(["a", "b", "a"])


def test_empty_symbol():
    with pytest.raises(ValueError):
        Alphabet(["a", ""])

# SI L'ALPHABET CONTIENT DES CHAINES ET DES LETTRE EN MM TEMPS
def test_non_string_symbol():
    with pytest.raises(TypeError):
        Alphabet(["a", 2])

#SI L'ALPHABET ENTREZ C'EST UNE CHAINE ET NON UNE COLLECTION
def test_string_is_not_a_collection_of_symbols():
    with pytest.raises(TypeError):
        Alphabet("abc")