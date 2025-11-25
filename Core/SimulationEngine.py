import time
from queue import Queue


# Importa os teus agentes
# from Core.Agents.Specific.MazeAgent import MazeAgent

class SimulationEngine:
    def __init__(self):
        self.agents = []
        self.action_mailbox = Queue()  # Onde o MCP recebe as ações
        self.running = True

    def create_agent(self, agent_instance):
        # Configura o canal de comunicação
        agent_instance.action_queue = self.action_mailbox
        self.agents.append(agent_instance)

    def run(self):
        print("--- MCP: A iniciar Simulação ---")

        for agent in self.agents:
            agent.start()

        step = 0
        while self.running and step < 5:
            print(f"\n--- Passo {step} ---")

            for agent in self.agents:
                agent.start_turn_signal.set()

            actions_received = 0
            while actions_received < len(self.agents):
                # Fica bloqueado aqui até receber mensagem
                agent_name, action = self.action_mailbox.get()
                print(f"MCP: Recebi ação '{action}' de {agent_name}")
                actions_received += 1

            # C. Atualizar o Ambiente (Só acontece quando todos jogaram)
            print("MCP: A atualizar o ambiente...")
            # self.environment.update(actions)

            time.sleep(1)  # Só para veres o output com calma
            step += 1

        # D. Matar as threads no fim
        self.stop_agents()

    def stop_agents(self):
        for agent in self.agents:
            agent.running = False
            agent.start_turn_signal.set()  # Acordar para eles verem o running=False
            agent.join()
        print("Simulação terminada.")