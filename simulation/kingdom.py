import agents
from agents import peasant

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

        dead_agent = []
        for active_agent in self.agents:
            state = active_agent.step(self)

            if state == "dead":
                dead_agent.append(active_agent)
            elif state == "reproduce":
                self.agent_born()

        self.agents = [a for a in self.agents if a not in dead_agent]





        #ONE TICK IS ONE HOUR
        self.tick += 1

        for agent in self.agents:
            agent.update()



        #EVERY WEEK
        if self.tick % 168 == 0:
            #STATISTIC TRACKING
            self.pop_list.append(len(self.agents))
            self.food_list.append(self.food_stores)

        #EVERY MONTH
        if self.tick % 720 == 0:
            self.treasury += math.floor(len(self.agents) * 0.2)
            print("population is: ", len(self.agents), "\nfood stores are: ", self.food_stores, "\ntreasury is: ", self.treasury)
    #END OF STEP FUNCTION

    def spawn_agents(self, amount):

        for _ in range(amount):
            peasant = Peasant(self.tick, self.map)
            #print("agent created and it is a ", peasant.gender)
            #print("agent is ", peasant.age, "years old and will die when they are ", peasant.ageofdeath)

            self.agents.append(peasant)
    #END OF SPAWN AGENTS FUNCTION

    def agent_born(self):
        peasant = Peasant(self.tick, self.map)
        # print("agent born")
        self.agents.append(peasant)
    #END OF AGENT BORN FUNCTION

    # 0 is Winter, 1 is Spring, 2 is Summer, 3 is Autumn
    def get_season(self):
        if (self.tick % 8760) // 2190 == 0:
            return "Winter"
        elif (self.tick % 8760) // 2190 == 1:
            return "Spring"
        elif (self.tick % 8760) // 2190 == 2:
            return "Summer"
        elif (self.tick % 8760) // 2190 == 3:
            return "Autumn"



