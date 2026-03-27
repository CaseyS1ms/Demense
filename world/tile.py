class Tile:

    TILE_PROPERTIES = \
        {
        "water": {"passable": False, "fertility": 0.0},
        "mountain": {"passable": False, "fertility":0.0},
        "forest":{"passable": True, "fertility":0.3},
        "farmland":{"passable": True, "fertility":1.0},
        "hills":{"passable": True, "fertility": 0.1}
        }

    def __init__(self, tileType):
        self.tileType = tileType
        self.passable = self.TILE_PROPERTIES[self.tileType]["passable"]
        self.fertility = self.TILE_PROPERTIES[self.tileType]["fertility"]

    def __str__(self):
        return self.tileType

