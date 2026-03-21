from world.map import Map as mp
from renderer.render import renderer
from simulation.kingdom import Kingdom

MAP_SIZE_WIDTH = 80
MAP_SIZE_HEIGHT = 80


world_map = mp(MAP_SIZE_WIDTH,MAP_SIZE_HEIGHT,12)
game_renderer = renderer(MAP_SIZE_WIDTH, MAP_SIZE_HEIGHT)
kingdom = Kingdom(0, 100, 0, 100, 1000, 50)

#SETTING UP THE SIM

world_map.generate()
#world_map.printMap()
game_renderer.initialise()



#WHILE RUNNING
running = True
while running:
    kingdom.step()
    if not game_renderer.update(world_map):
        running = False


