from abc import ABC

from Core.Agents.Base import BaseAgent


class Agent(BaseAgent, ABC):

    def __init__(self, name: str):
        super().__init__(name)
        pass