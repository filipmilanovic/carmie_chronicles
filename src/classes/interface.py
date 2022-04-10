from classes.map import Map
from classes.player import Player


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
        self.player = Player(self.map)

    def get_actions(self):
        self.player.current_screen.print()
        print(f'What would you like to do? {self.player.get_actions()}')

    def perform_action(self,
                       key_input: str):
        self.player.perform_action(key_input)
