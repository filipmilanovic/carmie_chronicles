import json
import random

from classes.map import Map
from classes.player import Player

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
        self.actions = None
        self.current_cell = None

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

        self.current_cell = random.choice(self.map.cells)
        self.current_cell.update_appearance(True)
        self.map.generate_grid()

    # ACTIONS
    def get_actions(self):
        current_screen_name = screen_map[self.current_screen.__class__.__name__].split('.')
        action_object = self
        for i in range(len(current_screen_name) - 1):
            action_object = getattr(action_object, current_screen_name[i])

        getattr(action_object, current_screen_name[-1]).set_actions()
        self.actions = getattr(action_object, current_screen_name[-1]).actions.actions_display
        self.current_screen.print_screen()
        
        print(f'What would you like to do? {self.actions}')

    def perform_action(self,
                       key_input: str):
        current_screen_name = screen_map[self.current_screen.__class__.__name__].split('.')

        action_object = self
        for i in range(len(current_screen_name) - 1):
            action_object = getattr(action_object, current_screen_name[i])
        
        getattr(action_object, current_screen_name[-1]).perform_action(self, key_input)
