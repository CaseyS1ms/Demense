import pygame
import random


class renderer:

    TILE_SIZE = 2

    TILE_COLOR = \
        {
            "water": (137, 207, 240),
            "mountain": (113, 113, 123),
            "farmland": (124, 207, 53),
            "forest":  (53, 83, 14),
            "hills":  (187, 244, 81)
        }



    def __init__(self, width, height):
        self.tile_colour = None
        self.screen = None
        self.size = None
        # self.map_size = map_size
        self.width = width
        self.height = height
        self.rndomChance = random.randint(0,1)
        self.clock = 0





    def initialise(self):
        pygame.init()

        self.sizeW = self.width
        self.sizeH = self.height
        self.screen = pygame.display.set_mode((self.sizeW, self.sizeH))
        self.map_surface = None


        #temporarily here
        self.clock = pygame.time.Clock()
        self.screen.fill("white")




    def update(self, world_map, agents):

        self.screen.blit(self.map_surface, (0, 0))


        for agent in agents:
            pygame.draw.circle(self.screen, "red", (agent.posX * self.TILE_SIZE, agent.posY * self.TILE_SIZE), 2)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                return False


        self.clock.tick(60)

        return True



    def draw_map(self, world_map):
        self.map_surface = pygame.Surface((world_map.width * self.TILE_SIZE, world_map.height * self.TILE_SIZE))
        for y in range(world_map.height):
            for x in range(world_map.width):
                tile = world_map.grid[y][x]
                self.tile_colour = self.TILE_COLOR[tile.tileType]
                pygame.draw.rect(self.map_surface,self.tile_colour, (x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))










