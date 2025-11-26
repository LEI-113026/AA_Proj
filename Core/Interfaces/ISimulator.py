from abc import ABC, abstractmethod
from Core.Interfaces.IAgent import IAgent


class ISimulator(ABC):
    @abstractmethod
    def create(self, filename: str) -> "ISimulator":
        pass

    @abstractmethod
    def list_agents(self) -> list[IAgent]:
        pass

    @abstractmethod
    def execute(self):
        pass