import agents

from agents.peasant import Peasant
from simulation.simulator import Simulator
import random
import math

class Kingdom(Simulator):

    def __init__(self, map, market, agents, food_stores, treasury):
        super().__init__(map, market, agents, len(agents), food_stores, treasury)
        self.pop_list = []
        self.food_list = []

    def step(self):
        self.tick += 1

        for agent in self.agents:
            agent.posX += random.randint(-1,1)
            agent.posY += random.randint(-1,1)

            if agent.posX > 800:
                agent.posX = 0
            elif agent.posY > 800:
                agent.posY = 0

        #EVERY DAY
        if self.tick % 24 == 0:
            pass

        #EVERY WEEK
        if self.tick % 168 == 0:
            self.pop_list.append(len(self.agents))
            self.food_list.append(self.food_stores)

        #EVERY MONTH

        if self.tick % 720 == 0:
            self.treasury += math.floor(len(self.agents) * 0.2)

            print("population is: ", len(self.agents), "\nfood stores are: ", self.food_stores, "\ntreasury is: ", self.treasury)


    def spawn_agents(self, amount):

        for _ in range(amount):
            peasant = Peasant(self.tick)
            print("agent created and it is a ", peasant.gender)
            print("agent is ", peasant.age, "years old and will die when they are ", peasant.ageofdeath)

            self.agents.append(peasant)
            # print(len(self.agents))

    def agent_born(self):
        peasant = Peasant(self.tick)
        # print("agent born")
        self.agents.append(peasant)

    def agent_move(self, peasant):
        peasant.posX += 0.5 * random.randint(0,1)
        peasant.posY += 0.5 * random.randint(0,1)

