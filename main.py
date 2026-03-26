import matplotlib.pyplot as plt

from agents.peasant import Peasant
from world.map import Map as mp
from renderer.render import renderer
from simulation.kingdom import Kingdom


MAP_SIZE_WIDTH = 1000
MAP_SIZE_HEIGHT = 1000


world_map = mp(MAP_SIZE_WIDTH,MAP_SIZE_HEIGHT,100)
game_renderer = renderer(MAP_SIZE_WIDTH, MAP_SIZE_HEIGHT)
kingdom = Kingdom(world_map, 100, [],  100, 50)

#SETTING UP THE SIM

world_map.generate()
#world_map.printMap()
game_renderer.initialise()
game_renderer.draw_map(world_map)
kingdom.spawn_agents(10)






#WHILE RUNNING
running = True
while running:

    kingdom.step()
    dead_agent = []
    for active_agent in kingdom.agents:
        state = active_agent.step(kingdom)

        if state == "dead":
            dead_agent.append(active_agent)
        elif state == "reproduce":
            kingdom.agent_born()


    kingdom.agents = [a for a in kingdom.agents if a not in dead_agent]


    if not game_renderer.update(world_map, kingdom.agents):
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


