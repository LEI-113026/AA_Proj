from abc import ABC, abstractmethod

from Core.Models import Sensor
from Core.Models.Observation import Observation
from Core.Models.Action import Action


class IAgent(ABC):
    @abstractmethod
    def create(self, filename: str) -> "IAgent":
        pass

    @abstractmethod
    def perceive(self, obs: Observation):
        pass

    @abstractmethod
    def act(self) -> Action:
        pass

    @abstractmethod
    def current_state_evaluation(self, reward: float):
        pass

    @abstractmethod
    def install(self, sensor: Sensor):
        pass

    @abstractmethod
    def communicate(self, message: str, from_agent: "IAgent"):
        pass