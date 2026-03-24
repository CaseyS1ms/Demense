from agents.agent import Agent
import random


class Peasant(Agent):

    def __init__(self, tick):
        super().__init__(0, 0, tick, 0)
        self.last_reproduced = random.randint(0,6480)
        self.ageofdeath = random.randint(60, 100)



#One Tick is one hour

    def step(self, simulator):

        #HUNGER INCREMENTING
        self.hunger += 0.5

        #SURVIVAL CHECKS
        if self.hunger >= 100:
            print("agent died of hunger")
            return "dead"

        if self.age > self.ageofdeath:
            print("agent died of old age")
            return "dead"

        #EATING
        if self.hunger > 75:
            if self.attempt_eat(simulator):
                self.hunger = 0

        #REPRODUCTION
        if self.age >= 18 and self.gender == 2:  #Gender 2 is female
            if self.hunger < 75:
                if simulator.tick - self.last_reproduced > 6480:
                    if random.random() < 0.2:
                        # print("trying to reproduce")
                        self.last_reproduced = simulator.tick
                        return "reproduce"

        #AGING - every year
        if simulator.tick % 8760 == 0:
            self.age += 1

        return "alive"







    def attempt_eat(self,simulator):
        if simulator.is_food():
            simulator.food_stores -= 1
            return True
        else:
            return False