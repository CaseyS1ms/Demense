from agents.agent import Agent
import random


class Peasant(Agent):

    def __init__(self, tick, sim_map):
        super().__init__(0, 0, tick, 0, sim_map)
        self.last_reproduced = random.randint(0,6480)
        self.ageofdeath = random.randint(60, 100)
        self.birth_tick = tick
        self.sim_map = sim_map



#One Tick is one hour

    def step(self, simulator):

        #HUNGER INCREMENTING
        self.hunger += 1

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

        #WORKING - making food every day
        if (simulator.tick - self.birth_tick) % 72 == 0:
            simulator.food_stores += 1

        #AGING - every year
        if simulator.tick % 8760 == 0:
            self.age += 1

        return "alive"


    def update(self):
        self.posX += random.randint(-1, 1)
        self.posY += random.randint(-1,1)

        if self.posX > self.sim_map.width:
            self.posX = 0
        elif self.posY > self.sim_map.height:
            self.posY = 0


    # def agent_move(self, peasant):
    #     peasant.posX += 0.5 * random.randint(0,1)
    #     peasant.posY += 0.5 * random.randint(0,1)




    def attempt_eat(self,simulator):
        if simulator.is_food():
            simulator.food_stores -= 1
            return True
        else:
            return False

