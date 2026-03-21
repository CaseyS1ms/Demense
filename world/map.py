import noise
import numpy as np
from world.tile import Tile

class Map:




    def __init__(self, width, height, scale):
        self.width = width
        self.height = height
        self.scale = scale

        self.grid = np.zeros((height,width), dtype=object)


    def generate(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = noise.pnoise2(x / self.scale, y / self.scale)
                tileType = self.getTileType(self.grid[y][x])
                self.grid[y][x] = Tile(tileType)
        return self.grid

    def getTileType(self, value):
        if value < -0.4:
            return "water"
        elif value < 0.0:
            return "farmland"
        elif value < 0.2:
            return "forest"
        elif value < 0.6:
            return "hills"
        else:
            return "mountain"


    def printMap(self):
        for y in range(self.height):
            tiles = []
            for x in range(self.width):
                tileType = self.grid[y][x]
                # print(tileType)
                tiles.append(tileType.tileType)
            print(tiles)



