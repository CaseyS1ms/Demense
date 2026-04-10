from world.map import Map as mp
from renderer.render import Renderer
from simulation.kingdom import Kingdom


#SETTING UP THE SIM

MAP_SIZE_WIDTH = 400
MAP_SIZE_HEIGHT = 300

game_renderer = Renderer(MAP_SIZE_WIDTH, MAP_SIZE_HEIGHT)
game_renderer.initialise()

map_width, map_height = game_renderer.get_map_dimensions()
world_map = mp(int(map_width),int(map_height),100)
world_map.generate()

kingdom = Kingdom(world_map, 100, [],  100, 50)
for i in range(1):
    kingdom.place_granary()
game_renderer.draw_map(world_map)





kingdom.spawn_agents(100)




STEPS_PER_FRAME = 1

#WHILE RUNNING
running = True
while running:

    for i in range(STEPS_PER_FRAME):
        kingdom.step()




    if not game_renderer.update(kingdom.agents, kingdom):
        running = False


