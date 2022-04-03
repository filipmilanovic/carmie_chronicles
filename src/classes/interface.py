from src.classes.maps import Map
from src.classes.players import Player


class Interface:
    """generate the game Interface to the backend classes"""
    def __init__(self):
        self.map = None
        self.player = None
        self.actions = None

    def generate_map(self,
                     rows: int,
                     cols: int,
                     towns: int):
        self.map = Map(rows=rows,
                       cols=cols,
                       towns=towns)

    def generate_player(self):
        self.player = Player(map_hash=self.map.hash)

    def get_actions(self):
        # ActionSet.update_actions(self.player)
        return f'What would you like to do? {self.player.actions.actions_display}'
