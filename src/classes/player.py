import json
import random

from classes.player_inventory import PlayerInventory

with open('src/dicts/attribute.json', 'r') as file:
    attributes = json.load(file)

player_dict = {}


class Player:
    def __init__(self,
                 starting_map):
        self.hash = hash(self)

        # PLAYER STATS
        self.set_default_stats()

        # PLAYER EQUIPPED
        self.weapon = None
        self.shield = None
        self.head = None
        self.body = None
        self.legs = None

        # PLAYER INVENTORY
        self.player_inventory = PlayerInventory(self)
        self.selected_item = None

        # LOCATION INFORMATION
        self.map = starting_map
        self.current_cell = random.choice(self.map.cells)
        self.current_cell.update_appearance(True)
        self.map.generate_grid()

        # ACTIONS
        self.current_screen = self.map
        self.path_to_screen = [self.current_screen]

    """CHARACTER INFORMATION"""
    def set_default_stats(self):
        [setattr(self, attr['name'], attr['default']) for attr in attributes.values()]

    """ACTIONS"""
    def get_actions(self):
        if self.current_screen.__class__.__name__ == 'Map':
            self.current_cell.set_actions()
            return self.current_cell.actions.actions_display
        elif self.current_screen.__class__.__name__ == 'PlayerInventory':
            self.player_inventory.set_actions()
            return self.player_inventory.actions.actions_display
        elif self.current_screen.__class__.__name__ == 'Equipment':
            self.selected_item.set_actions()
            return self.selected_item.actions.actions_display

    def perform_action(self,
                       key_input: str):
        if self.current_screen.__class__.__name__ == 'Map':
            self.current_cell.perform_action(self, key_input)
        elif self.current_screen.__class__.__name__ == 'PlayerInventory':
            self.player_inventory.perform_action(key_input)
        elif self.current_screen.__class__.__name__ == 'Equipment':
            self.selected_item.perform_action(self, key_input)
