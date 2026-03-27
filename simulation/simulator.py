class Simulator:

    def __init__(self,map, market, agents, population, food_stores, treasury):
        self.map = map
        self.agents = agents
        self.population = population
        self.food_stores = food_stores
        self.treasury = treasury
        self.season = 0
        self.tick = 0


    def step(self):
        raise NotImplementedError("Each Sim needs its own implementation")


    def is_food(self):
        if self.food_stores > 0:
            return True
        else:
            return False
