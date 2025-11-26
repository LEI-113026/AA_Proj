from dataclasses import dataclass
from Core.Models.ObjectInfo import ObjectInfo

@dataclass
class AgentInfo(ObjectInfo):
    """ Representa um agente para desenho """
    points: int = 0
    # Podes adicionar 'team_color', 'id', etc. aqui