import random

class Agent:


    def __init__(self, hunger, gold, tick, food):
        self.hunger = hunger
        self.gold = gold
        self.tick = tick
        self.food = 0
        self.posX = random.randint(10,750)
        self.posY = random.randint(10,750)


    def step(self, kingdom):
        raise NotImplementedError