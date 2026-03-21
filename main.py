from world.map import Map as mp
from renderer.render import renderer

MAP_SIZE = 80


world_map = mp(MAP_SIZE,MAP_SIZE,25)
game_renderer = renderer(MAP_SIZE)

world_map.generate()
#world_map.printMap()
game_renderer.initialise()
