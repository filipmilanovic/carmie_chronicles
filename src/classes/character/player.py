import json

from classes.character.attributes import Attributes
from classes.character.inventory import Inventory, Equipment

player_dict = {}


class Player:
    def __init__(self):
        self.hash = hash(self)

        # PLAYER EQUIPMENT
        self.weapon = None
        self.shield = None
        self.head = None
        self.body = None
        self.legs = None
        
        # PLAYER INVENTORY
        self.attributes = Attributes()
        self.inventory = Inventory()
        self.selected_item = None

        # SET STARTING EQUIPMENT
        self.inventory.add_item(self, Equipment('dagger', 'basic'), True)
        self.inventory.add_item(self, Equipment('shirt', 'basic'), True)
        self.inventory.add_item(self, Equipment('pants', 'basic'), True)
