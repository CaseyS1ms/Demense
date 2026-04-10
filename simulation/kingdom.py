from agents.peasant import Peasant
from simulation.simulator import Simulator
import random
import math
from structures.granary import Granary


class Kingdom(Simulator):

    def __init__(self, map, market, agents, food_stores, treasury):
        super().__init__(map, market, agents, len(agents), food_stores, treasury)
        self.pop_list = []
        self.food_list = []
        self.granary = None
        self.map = map
        self.total_births = 0
        self.total_deaths = 0

    def step(self):


        for active_agent in self.agents:
            state = active_agent.step(self)

            if state == "dead":
                self.total_deaths += 1
            elif state == "reproduce":
                self.agent_born()
                self.total_births += 1

        self.agents = [a for a in self.agents if a.is_alive]





        #ONE TICK IS ONE HOUR
        self.tick += 1







        #EVERY WEEK
        if self.tick % 168 == 0:
            #STATISTIC TRACKING
            self.pop_list.append(len(self.agents))
            self.food_list.append(self.food_stores)

        #EVERY MONTH
        if self.tick % 720 == 0:
            self.treasury += math.floor(len(self.agents) * 0.2)
            #print("population is: ", len(self.agents), "\nfood stores are: ", self.food_stores, "\ntreasury is: ", self.treasury)
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
    #END OF AGENT-BORN FUNCTION

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
    #END OF GET SEASON FUNCTION


    def place_granary(self):
        tile_list = [(x, y) for y in range(self.map.height) for x in range(self.map.width)]
        random.shuffle(tile_list)
        for x,y in tile_list:
            if self.map.grid[y][x].passable and self.map.grid[y][x].fertility >= 1:
                self.granary = Granary(x, y)
                tile = self.map.grid[y][x]
                tile.tile_state = "taken"
                return

        raise ValueError ("No Suitable Tile found")




