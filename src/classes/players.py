import json
import random
from src.classes.actions import ActionSet
from src.classes.equipment import Equipment
from src.classes.maps import map_dict

with open('../src/dicts/attributes.json', 'r') as file:
    attributes = json.load(file)

with open('../src/dicts/weapons.json', 'r') as file:
    weapons = json.load(file)

with open('../src/dicts/armour.json', 'r') as file:
    armour = json.load(file)

player_dict = {}


class Player:
    def __init__(self,
                 map_hash: int):
        self.hash = hash(self)

        # Player stats
        self.set_default_stats()

        # Player equipped
        self.weapon = None
        self.shield = None
        self.head = None
        self.body = None
        self.legs = None

        # Player inventory
        self.inventory = []
        [self.add_item(Equipment(item)) for item in weapons.values() if item['item_id'] in [1000]]
        [self.add_item(Equipment(item)) for item in armour.values() if item['item_id'] in [2000, 3000, 4000]]

        # Map and Screen information
        self.map = map_dict[map_hash]
        self.current_cell = random.choice(self.map.cells)
        self.current_cell.update_appearance(True)
        self.map.generate_grid()

        # Actions
        self.current_screen = 'map'
        self.actions = ActionSet(self)
        self.actions.set_actions()

    """CHARACTER INFORMATION"""
    def set_default_stats(self):
        [setattr(self, attr['name'], attr['default']) for attr in attributes.values()]

    """MOVEMENT"""

    """INVENTORY"""
    def add_item(self,
                 item):
        self.inventory.append(item)

    def show_inventory(self):
        print([[item.info['name'], item.info['class']] for item in self.inventory])

    """EQUIPMENT"""
    def equip_item(self,
                   equipment_dict: dict,
                   equipment_name: str):
        item = Equipment(equipment_dict[equipment_name])
        setattr(self, item.info['class'], item)

    def show_equipment(self):
        print(f'''
                       ___ {self.head}
                      |   |
                      |   |   |
                       ---    | {self.weapon}
                        |     |
                   -----------|
                        |
                        |  {self.body}
                        |
                       / \\
                      /   \\    {self.legs}
                     /     \\ ''')
