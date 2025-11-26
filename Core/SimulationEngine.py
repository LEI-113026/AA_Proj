import time
from queue import Queue


class SimulationEngine:
    def __init__(self):
        self.agents = {}

        self.services = {}

        self.action_mailbox = Queue()
        self.running = True

    def create_agent(self, agent_instance):
        if agent_instance.name in self.agents:
            print(f"Erro: Agente {agent_instance.name} já existe!")
            return

        agent_instance.action_queue = self.action_mailbox
        self.agents[agent_instance.name] = agent_instance

        if hasattr(agent_instance, 'services'):
            for service in agent_instance.services:
                if service not in self.services:
                    self.services[service] = []
                self.services[service].append(agent_instance.name)

    def list_agents(self):
        """ Funcionalidade de White Pages """
        return list(self.agents.values())

    def find_agent(self, name):
        """ Busca nas White Pages """
        return self.agents.get(name)

    def find_service_providers(self, service_name):
        """ Busca nas Yellow Pages """
        names = self.services.get(service_name, [])
        return [self.agents[name] for name in names]

    def run(self):
        print("--- MCP: A iniciar Simulação ---")
        for agent in self.agents.values():
            agent.start()

        step = 0
        while self.running and step < 5:
            print(f"\n--- Passo {step} ---")

            for agent in self.agents.values():
                agent.start_turn_signal.set()

            actions_received = 0
            while actions_received < len(self.agents):
                agent_name, action = self.action_mailbox.get()
                print(f"MCP: Recebi ação '{action}' de {agent_name}")
                actions_received += 1


            time.sleep(1)
            step += 1

        self.stop_agents()

    def stop_agents(self):
        for agent in self.agents.values():
            agent.running = False
            agent.start_turn_signal.set()
            agent.join()