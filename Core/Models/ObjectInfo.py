from dataclasses import dataclass

@dataclass
class ObjectInfo:
    """ Representa um objeto estático (parede, recurso) para desenho """
    x: int
    y: int
    symbol: str