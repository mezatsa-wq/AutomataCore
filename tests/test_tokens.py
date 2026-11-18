import pytest
from dataclasses import FrozenInstanceError

from coeur.tokens import Token


def test_create_token():

    token = Token("SYMBOL", "a", 1)

    assert token.kind == "SYMBOL"
    assert token.value == "a"
    assert token.position == 1


def test_token_is_immutable():

    token = Token("SYMBOL", "a", 1)

    with pytest.raises(FrozenInstanceError):
        token.value = "b"