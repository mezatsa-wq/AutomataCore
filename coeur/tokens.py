from dataclasses import dataclass
@dataclass(frozen=True)
class Token:
    """note bien: !r rajouter automatiquement des guillemets autour de la valeur qui le preceder et demande a python d'utiliser la representation officielle de lojet et non la representation classique
    represente une unite lexicale.
    kind represente le type du token.
    value represente la valeur du token.
    position represente la position de l'expression original."""
    kind: str
    value: str
    position: int