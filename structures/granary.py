from structures.structure import Structure


class Granary(Structure):

    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.food_storage = 0
