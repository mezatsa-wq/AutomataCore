import pytest

from coeur.alphabet import Alphabet
from coeur.analyseur_lexical import Lexer


def get_kinds(expression, symbols):
    alphabet = Alphabet(symbols)
    lexer = Lexer(expression, alphabet)
    return lexer.tokenize()


def test_simple_symbols():
    tokens = get_kinds("ab", ["a", "b"])

    assert [t.kind for t in tokens] == [
        "SYMBOL", "SYMBOL"
    ]


def test_union():
    tokens = get_kinds("a|b", ["a", "b"])

    assert [t.kind for t in tokens] == [
        "SYMBOL", "UNION", "SYMBOL"
    ]


def test_star():
    tokens = get_kinds("a*", ["a"])

    assert [t.kind for t in tokens] == [
        "SYMBOL", "STAR"
    ]


def test_parentheses():
    tokens = get_kinds("(a|b)", ["a", "b"])

    assert [t.kind for t in tokens] == [
        "LEFT_PAREN",
        "SYMBOL",
        "UNION",
        "SYMBOL",
        "RIGHT_PAREN",
    ]


def test_explicit_concat():
    tokens = get_kinds("a.b", ["a", "b"])

    assert [t.kind for t in tokens] == [
        "SYMBOL", "CONCAT", "SYMBOL"
    ]


def test_multi_character_symbol():
    tokens = get_kinds("{bonjour}", ["bonjour"])

    assert len(tokens) == 1
    assert tokens[0].value == "bonjour"


def test_escaped_operator():
    tokens = get_kinds(r"a\*", ["a", "*"])

    assert [t.kind for t in tokens] == [
        "SYMBOL", "SYMBOL"
    ]

    assert tokens[1].value == "*"


def test_escaped_backslash():
    tokens = get_kinds(r"\\", ["\\"])

    assert len(tokens) == 1
    assert tokens[0].value == "\\"


def test_unknown_symbol():
    with pytest.raises(ValueError):
        get_kinds("ax", ["a", "b"])


def test_missing_closing_brace():
    with pytest.raises(ValueError):
        get_kinds("{bonjour", ["bonjour"])


def test_empty_braces():
    with pytest.raises(ValueError):
        get_kinds("{}", ["bonjour"])


def test_unexpected_closing_brace():
    with pytest.raises(ValueError):
        get_kinds("}", ["a"])


def test_epsilon():
    tokens = get_kinds("ε", ["a"])

    assert len(tokens) == 1
    assert tokens[0].kind == "EPSILON"


def test_whitespace():
    tokens = get_kinds("a | b", ["a", "b"])

    assert [t.kind for t in tokens] == [
        "SYMBOL", "UNION", "SYMBOL"
    ]
def test_character_class():

    alphabet = Alphabet(["a", "b", "c"])

    tokens = Lexer("[a-b]b", alphabet).tokenize()

    assert tokens[0].kind == "CHARACTER_CLASS"
    assert tokens[0].value == ("a", "b")

    assert tokens[1].kind == "SYMBOL"
    assert tokens[1].value == "b"


def test_character_set():

    alphabet = Alphabet(["a", "b", "c"])

    tokens = Lexer("[abc]", alphabet).tokenize()

    assert tokens[0].kind == "CHARACTER_CLASS"
    assert tokens[0].value == ("a", "b", "c")


def test_alphabet_missing_range_symbol():

    alphabet = Alphabet(["a", "b"])

    with pytest.raises(ValueError):
        Lexer("[a-c]", alphabet).tokenize()
def test_invalid_range_order():

    alphabet = Alphabet(["a", "b", "c"])

    with pytest.raises(ValueError):
        Lexer("[c-a]", alphabet).tokenize()


def test_empty_character_class():

    alphabet = Alphabet(["a", "b"])

    with pytest.raises(ValueError):
        Lexer("[]", alphabet).tokenize()


def test_missing_closing_bracket():

    alphabet = Alphabet(["a", "b"])

    with pytest.raises(ValueError):
        Lexer("[a-b", alphabet).tokenize()


def test_escaped_hyphen():

    alphabet = Alphabet(["a", "-"])

    tokens = Lexer(r"[a\-]", alphabet).tokenize()

    assert tokens[0].kind == "CHARACTER_CLASS"
    assert tokens[0].value == ("a", "-")


def test_reversed_range():

    alphabet = Alphabet(["a", "b", "c"])

    with pytest.raises(ValueError):
        Lexer("[b-a]", alphabet).tokenize()
