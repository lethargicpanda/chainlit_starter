from agents.base_agent import Agent

class ImplementationAgent(Agent):

    def __init__(self, name, client, prompt=""):
        super().__init__(name, client, prompt)


    # def implement(self, task):
    #     print(f"{self.name} is implementing: {task}")
    #     # Add implementation logic here