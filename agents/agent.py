import random

class Agent:


    def __init__(self, hunger, gold, tick, food, map):
        self.hunger = hunger
        self.gold = gold
        self.tick = tick
        self.food = 0
        self.posX = random.randint(10,map.width)
        self.posY = random.randint(10,map.height)
        self.age = random.randint(18, 24)
        self.gender = random.randint(1,2) #1 is male 2 is female - will play a role in reproduction
        self.map = map
        self.state = "idle"

        self.find_spawn_position()

    def step(self, kingdom):
        raise NotImplementedError

    def find_spawn_position(self):
        max_y, max_x = self.map.grid.shape

        while True:
            self.posX = random.randrange(0, max_x)
            self.posY = random.randrange(0, max_y)

            if self.map.grid[self.posY][self.posX].passable:
                break