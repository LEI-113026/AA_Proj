from dataclasses import dataclass
from Core.Models.ObjectInfo import ObjectInfo

@dataclass
class AgentInfo(ObjectInfo):
    points: int = 0