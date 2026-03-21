import pygame



class renderer:

    TILE_SIZE = 10



    def __init__(self, map_size):
        self.screen = None
        self.size = None
        self.map_size = map_size




    def initialise(self):
        pygame.init()

        self.size = self.TILE_SIZE * self.map_size
        self.screen = pygame.display.set_mode((self.size, self.size))

        #temporarily here
        clock = pygame.time.Clock()
        self.screen.fill("white")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

            clock.tick(60)


    def update(self, world_map):
        for y in range(self.size):
            for x in range(self.size):





