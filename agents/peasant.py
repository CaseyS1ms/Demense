from agents.agent import Agent
import random

from structures import granary


class Peasant(Agent):

    def __init__(self, tick, sim_map):
        super().__init__(0, 0, tick, 0, sim_map)
        self.last_reproduced = random.randint(0,6480)
        self.update_offset = random.randint(0, 5)
        self.ageofdeath = random.randint(60, 100)
        self.birth_tick = tick
        self.sim_map = sim_map
        self.time_started = 0



#One Tick is one hour

    def step(self, simulator):

        #HUNGER INCREMENTING
        self.hunger += 1



        #SURVIVAL CHECKS
        if self.hunger >= 100:
            #print("agent died of hunger")
            self.is_alive = False
            return 'dead'

        if self.age > self.ageofdeath:
            #print("agent died of old age")
            self.is_alive = False
            return 'dead'

        #EATING
        if self.hunger > 35:
            if self.attempt_eat(simulator) and self.is_on_target(simulator.granary):
                self.hunger = 0
            # if self.attempt_eat(simulator):
            #     self.hunger = 0
            else:
                self.update(simulator.granary)
        else:
            if simulator.tick % 6 == self.update_offset:  # CHANGE THIS LINE
                self.update(None)


        #STATE MACHINE
        if self.state == "plowing":
            self.time_started = self.tick
            self.plowing_state()

        




        #REPRODUCTION
        if self.age >= 18 and self.gender == 2:  #Gender 2 is female
            if self.hunger < 75:
                if simulator.tick - self.last_reproduced > 6480:
                    if random.random() < 0.2:
                        self.last_reproduced = simulator.tick
                        return "reproduce"

        #WORKING - making food every day
        if (simulator.tick - self.birth_tick) % 24 == 0:
            simulator.food_stores += 1.2

        #AGING - every year
        if (simulator.tick - self.birth_tick) % 8760 == 0 and simulator.tick != self.birth_tick:
            self.age += 1

        return "alive"
    #END OF STEP FUNCTION

    def update(self, target):

        max_x = self.sim_map.width - 1
        max_y = self.sim_map.height - 1

        new_x = self.posX
        new_y = self.posY

        if target is None:
            new_x = self.posX + random.randint(-1, 1)
            new_y = self.posY + random.randint(-1,1)
        else:
            if random.random() < 0.8:

                if self.posX < target.posX:
                    new_x = self.posX + 1
                if self.posX > target.posX:
                    new_x = self.posX - 1
                if self.posY < target.posY:
                    new_y = self.posY + 1
                if self.posY > target.posY:
                    new_y = self.posY - 1

        #BOUNDS CHECKING
        new_x = max(0, min(max_x, new_x))
        new_y = max(0, min(max_y, new_y))

        #CHECKING FOR IMPASSABLE TERRAIN
        if self.sim_map.grid[new_y][new_x].passable:
            self.posX = new_x
            self.posY = new_y
        else:
           pass



    #ENF OF UPDATE FUNCTION

    def attempt_eat(self,simulator):
        if simulator.is_food():
            simulator.food_stores -= 1
            simulator.food_stores = max(0, simulator.food_stores)
            return True
        else:
            return False

    def is_on_target(self, target):
        if self.posY == target.posY:
            if self.posX == target.posX:
                return True
            return False
        else:
            return False

    #END OF ATTEMPT EAT FUNCTION

    def plowing_state(self):
        #PLOWS TILE ITS ON
        if self.time_started - self.tick >= 2:
            tile = self.sim_map.grid[self.posY][self.posX]
            tile.tile_state = "plowed"