from abc import ABC, abstractmethod

from Core.Interfaces import IAgent
from Core.Models import Observation
from Core.Models.Action import Action


class IEnviroment(ABC):
    @abstractmethod
    def observation_to(self, agent: IAgent) -> Observation:
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def act(self, action: Action, agent: IAgent):
        pass