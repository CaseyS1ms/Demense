from agents.agent import Agent
import random


class Peasant(Agent):

    def __init__(self, tick):
        super().__init__(0, 0, tick, 0)
        self.last_reproduced = 0



#One Tick is one hour

    def step(self, simulator):

        self.hunger += 0.5

        if self.hunger >= 100:
            return "dead"


        if self.hunger > 75:
            if self.attempt_eat(simulator):
                self.hunger = 0

        if self.hunger < 75:
            if random.random() < 0.2:
                # print(simulator.tick, self.last_reproduced, simulator.tick - self.last_reproduced)

                if simulator.tick - self.last_reproduced > 6480:
                    # print("trying to reproduce")
                    self.last_reproduced = simulator.tick
                    return "reproduce"

        return "alive"







    def attempt_eat(self,simulator):
        if simulator.is_food():
            simulator.food_stores -= 1
            return True
        else:
            return False