import matplotlib.pyplot as plt

from agents.peasant import Peasant
from world.map import Map as mp
from renderer.render import renderer
from simulation.kingdom import Kingdom


MAP_SIZE_WIDTH = 500
MAP_SIZE_HEIGHT = 400

game_renderer = renderer(MAP_SIZE_WIDTH, MAP_SIZE_HEIGHT)
map_width, map_height = game_renderer.get_map_dimensions()
world_map = mp(int(map_width),int(map_height),25)

kingdom = Kingdom(world_map, 100, [],  100, 50)

#SETTING UP THE SIM

world_map.generate()
game_renderer.initialise()
game_renderer.draw_map(world_map)
kingdom.spawn_agents(10)






#WHILE RUNNING
running = True
while running:

    kingdom.step()



    if not game_renderer.update(kingdom.agents, kingdom):
        running = False

if kingdom.pop_list and kingdom.food_list:
    plt.figure(figsize=(10, 5))
    plt.plot(kingdom.food_list, label="Food Stores")
    plt.plot(kingdom.pop_list, label="Population")
    plt.title("Kingdom Growth Over Time")
    plt.xlabel("Weeks")
    plt.ylabel("Amount")
    plt.legend()
    plt.show()


