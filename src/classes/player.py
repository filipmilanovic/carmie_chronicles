import json

from classes.player_inventory import PlayerInventory

with open('src/dicts/attribute.json', 'r') as file:
    attributes = json.load(file)

player_dict = {}


class Player:
    def __init__(self):
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

    # CHARACTER INFORMATION
    def set_default_stats(self):
        [setattr(self, attr['name'], attr['default']) for attr in attributes.values()]
