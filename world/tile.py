class Tile:

    TILE_PROPERTIES = \
        {
        "water": {"passable": False, "fertility": 0.0},
        "mountain": {"passable": False, "fertility":0.0},
        "forest":{"passable": True, "fertility":0.3},
        "grass":{"passable": True, "fertility":1.0},
        "hills":{"passable": True, "fertility": 0.1}
        }

    def __init__(self, tileType):
        self.tileType = tileType
        self.passable = self.TILE_PROPERTIES[self.tileType]["passable"]
        self.fertility = self.TILE_PROPERTIES[self.tileType]["fertility"]
        self.crop = None
        self.tick_planted = None
        self.tile_state = None

    def __str__(self):
        return self.tileType

