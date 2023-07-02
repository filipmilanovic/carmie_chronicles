import json

from classes.map.map import Map
from classes.character.player import Player

with open('src/dicts/screen_map.json', 'r') as file:
    screen_map = json.load(file)

class Interface:
    """generate the game Interface to the backend classes"""
    def __init__(self):
        # CORE OBJECTS
        self.map = None
        self.player = None

        # CURRENT GAME STATUS
        self.current_screen = None
        self.path_to_screen = []

    # OBJECT GENERATION
    def generate_map(self,
                     rows: int,
                     cols: int,
                     towns: int):
        self.map = Map(rows=rows,
                       cols=cols,
                       towns=towns)
        self.current_screen = self.map
        self.path_to_screen.append(self.current_screen)

    def generate_player(self):
        self.player = Player()

    # ACTIONS
    def get_actions(self):
        action_attribute = screen_map[self.current_screen.__class__.__name__]

        action_object = getattr(self.current_screen, action_attribute) if action_attribute else self.current_screen
        action_object.set_actions()

        self.current_screen.gui.print_screen()
        print(f'What would you like to do? {action_object.actions.actions_display}')

    def perform_action(self,
                       key_input: str):
        action_attribute = screen_map[self.current_screen.__class__.__name__]

        action_object = getattr(self.current_screen, action_attribute) if action_attribute else self.current_screen
        action_object.perform_action(self, key_input)
