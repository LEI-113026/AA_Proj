import threading
from abc import ABC

from Core.Interfaces.IAgent import IAgent

class BaseAgent(IAgent, threading.Thread, ABC):

    def __init__(self, name: str):
        threading.Thread.__init__(self, name=name)

        self.running = False
        self.action_queue = None
        self.turn_signal = threading.Event()

        self.sensors = []

    def run(self):

        print(f"[{self.name}] Thread iniciada.")

        while self.running:
            self.turn_signal.wait()
            if not self.running: break
            self.turn_signal.clear()

            action = self.act()

            # 3. Enviar ação para o Motor
            if self.action_queue:
                self.action_queue.put((self.name, action))


    def communicate(self, message: str, from_agent: "IAgent"):
        print(f"[{self.name}] Recebi: {message}")