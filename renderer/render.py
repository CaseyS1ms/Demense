import pygame



class renderer:

    TILE_SIZE = 10

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





    def initialise(self):
        pygame.init()

        self.sizeW = self.TILE_SIZE * self.width
        self.sizeH = self.TILE_SIZE * self.height
        self.screen = pygame.display.set_mode((self.sizeW, self.sizeH))

        #temporarily here
        clock = pygame.time.Clock()
        self.screen.fill("white")




    def update(self, world_map):

        for y in range(world_map.height):
            for x in range(world_map.width):
                tile = world_map.grid[y][x]
                self.tile_colour = self.TILE_COLOR[tile.tileType]
                pygame.draw.rect(self.screen,self.tile_colour, (x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                return False


        return True









