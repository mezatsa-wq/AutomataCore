from dataclasses import dataclass


@dataclass(frozen=True)
class Symbol:
    value: str


@dataclass(frozen=True)
class CharacterClass:
    symbols: frozenset


@dataclass(frozen=True)
class Epsilon:
    pass


@dataclass(frozen=True)
class Union:
    left: object
    right: object


@dataclass(frozen=True)
class Concat:
    left: object
    right: object


@dataclass(frozen=True)
class Star:
    operand: object


@dataclass(frozen=True)
class Plus:
    operand: object


@dataclass(frozen=True)
class Optional:
    operand: object