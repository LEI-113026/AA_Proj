import threading
from abc import ABC

from Core.Interfaces.IAgent import IAgent
from Core.Models import Sensor


class BaseAgent(IAgent, threading.Thread, ABC):
    def __init__(self, name: str):
        threading.Thread.__init__(self, name=name)

        self.running = False
        self.action_queue = None
        self.turn_signal = threading.Event()
        self.points = 0

        self.sensors = []

    def run(self):
        print(f"[{self.name}] Thread iniciada.")

        while self.running:
            self.turn_signal.wait()
            if not self.running: break
            self.turn_signal.clear()
            action = self.act()
            if self.action_queue:
                self.action_queue.put((self.name, action))


    def communicate(self, message: str, from_agent: "IAgent"):
        print(f"[{self.name}] Recebi: {message}")

    def install(self, sensor: Sensor):
        self.sensors.append(sensor)

    def current_state_evaluation(self, reward: float):
        self.points += reward
