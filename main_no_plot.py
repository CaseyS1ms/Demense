from world.map import Map as mp
from renderer.render import renderer
from simulation.kingdom import Kingdom


#SETTING UP THE SIM

MAP_SIZE_WIDTH = 1000
MAP_SIZE_HEIGHT = 800

game_renderer = renderer(MAP_SIZE_WIDTH, MAP_SIZE_HEIGHT)
game_renderer.initialise()

map_width, map_height = game_renderer.get_map_dimensions()
world_map = mp(int(map_width),int(map_height),100)
world_map.generate()

game_renderer.draw_map(world_map)



kingdom = Kingdom(world_map, 100, [],  100, 50)
kingdom.spawn_agents(99999)






#WHILE RUNNING
running = True
while running:

    kingdom.step()



    if not game_renderer.update(world_map, kingdom.agents):
        running = False


