import agents

from agents.peasant import Peasant
from simulation.simulator import Simulator
import random
import math

class Kingdom(Simulator):

    def __init__(self, map, market, agents, food_stores, treasury):
        super().__init__(map, market, agents, len(agents), food_stores, treasury)







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

            # print("population is: ", self.population, "\nfood stores are: ", self.food_stores, "\ntreasury is: ",
            #       self.treasury)

            #PEOPLE EATING
            #self.food_stores = max(0, self.food_stores - self.population)
            #PEOPLE PRODUCING FOOD
            # self.food_stores += math.floor(len(self.agents)  * 1.2)

            #POPUlATION LOGIC
            # if self.food_stores > self.population * 1.5:
            #     if random.random() < 0.2:
            #         self.population += 1
            #         self.food_stores -= 1

        #EVERY 3 DAYS
            if self.tick % 72 == 0:
                self.food_stores += math.floor(len(self.agents)  * 0.9)
        #
        #     if self.food_stores < self.population:
        #         self.population = max(0, self.population - 1)


        #EVERY MONTH

        if self.tick % 720 == 0:
            self.treasury += math.floor(len(self.agents) * 0.2)

            print("population is: ", len(self.agents), "\nfood stores are: ", self.food_stores, "\ntreasury is: ", self.treasury)




        #EVERY HALF-YEAR A BIG HARVEST
        # if self.tick % 4380 == 0:
        #
        #     self.food_stores += 50 * 100




    def spawn_agents(self, amount):

        for _ in range(amount):
            peasant = Peasant(self.tick)
            print("agent created")
            self.agents.append(peasant)
            # print(len(self.agents))


    def agent_born(self):
        peasant = Peasant(self.tick)
        # print("agent born")
        self.agents.append(peasant)

    def agent_move(self, peasant):
        peasant.posX += 0.5 * random.randint(0,1)
        peasant.posY += 0.5 * random.randint(0,1)

