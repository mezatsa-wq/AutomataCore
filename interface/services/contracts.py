from dataclasses import dataclass, field
from typing import Any


@dataclass
class AnalysisResult:
    """Résultat de la validation de l'expression."""

    valid: bool
    tokens: list = field(default_factory=list)
    ast: Any = None
    message: str = ""


@dataclass
class AutomatonResult:
    """Résultat de construction d'un automate."""

    automaton: Any
    transitions: list = field(default_factory=list)
    image_path: str | None = None
    message: str = ""


@dataclass
class RecognitionResult:
    """Résultat de reconnaissance d'un mot."""

    accepted: bool
    trace: list = field(default_factory=list)
    message: str = ""


@dataclass
class ConstructionResult:
    """Résultat global de construction."""

    analysis: AnalysisResult
    nfa: AutomatonResult
    dfa: AutomatonResult