cell_dict = {}


class Cell:
    """a Cell class object denoting one region on the Map"""
    instances = []

    def __init__(self):
        self.hash = hash(self)
        cell_dict[self.hash] = self
        self.player_cell = False
        self.appearance = 'o'
        self.north_hash = None
        self.west_hash = None
        self.south_hash = None
        self.east_hash = None
        self.is_town = None

    def update_appearance(self,
                          player_cell: bool):
        """set the appearance of the Cell in the Map given its' attributes and the Player's location"""
        self.player_cell = player_cell

        if self.player_cell:
            self.appearance = 'x'
        elif self.is_town:
            self.appearance = 't'
        else:
            self.appearance = 'o'
