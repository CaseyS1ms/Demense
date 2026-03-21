from simulator import Simulator
import random
import math

class Kingdom(Simulator):

    def __init__(self, map, market, agents, population, food_stores, treasury):
        super().__init__(map, market, agents, population, food_stores, treasury)






    def step(self):
        self.tick += 1



        #EVERY DAY
        if self.tick % 24 == 0:

            print("population is: ", self.population, "\nfood stores are: ", self.food_stores, "\ntreasury is: ",
                  self.treasury)

            #PEOPLE EATING
            self.food_stores = max(0, self.food_stores - self.population)
            #PEOPLE PRODUCING FOOD
            #self.food_stores += math.floor(self.population  * 1.2)

            #POPUlATION LOGIC
            if self.food_stores > self.population * 1.5:
                if random.random() < 0.2:
                    self.population += 1
                    self.food_stores -= 1

        #EVERY 3 DAYS
        if self.tick % 72 == 0:

            if self.food_stores < self.population:
                self.population = max(0, self.population - 1)


        #EVERY MONTH

        if self.tick % 720 == 0:
            self.treasury += math.floor(self.population * 0.2)

            print("population is: ", self.population, "\nfood stores are: ", self.food_stores, "\ntreasury is: ", self.treasury)


        #EVERY HALF YEAR A BIG HARVEST
        if self.tick % 4380 == 0:

            self.food_stores += self.population * 100

