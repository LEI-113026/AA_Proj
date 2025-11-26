import os
import platform
from Core.Models.AgentInfo import AgentInfo
from Core.Models.ObjectInfo import ObjectInfo


def _clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)


class Drawing:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def draw(self, agents_info: list[AgentInfo], objects_info: list[ObjectInfo]):
        _clear_screen()
        grid = [['.' for _ in range(self.width)] for _ in range(self.height)]

        for obj in objects_info:
            if 0 <= obj.x < self.width and 0 <= obj.y < self.height:
                grid[obj.y][obj.x] = obj.symbol

        for agent in agents_info:
            if 0 <= agent.x < self.width and 0 <= agent.y < self.height:
                grid[agent.y][agent.x] = agent.symbol

        print(f"--- Simulação: {self.width}x{self.height} ---")
        for row in grid:
            print(" ".join(row))

        print("-" * (self.width * 2))
        for agent in agents_info:
            print(f"Agente ({agent.symbol}): {agent.points} pts | Pos: ({agent.x}, {agent.y})")