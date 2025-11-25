from Core.Agents.Base import BaseAgent
from Core.Models.Action import Action
from Core.Models.Observation import Observation


class Agent(BaseAgent):
    def act(self) -> Action:
        pass

    def perceive(self, obs: Observation):
        pass

    def create(self, filename: str):
        pass

    def __init__(self, filename: str):
        pass