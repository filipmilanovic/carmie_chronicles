import json
import math

from classes.shared.action import ActionSet
from gui.equipment import GUIEquipment

with open('src/dicts/equipment_class.json', 'r') as file:
    classes = json.load(file)

with open('src/dicts/equipment_collection.json', 'r') as file:
    collections = json.load(file)

with open('src/dicts/equipment_type.json', 'r') as file:
    types = json.load(file)


class Equipment:
    def __init__(self,
                 equipment_type,
                 equipment_collection):
        self.hash = hash(self)
        self.gui = GUIEquipment(self)

        self.equipment_type = equipment_type
        self.equipment_collection = equipment_collection
        self.id, self.info, self.stats = self.set_equipment_details()
        self.is_equipped = False

        self.actions = ActionSet()
        self.menu_back = True
        self.menu_equip = True
        self.menu_unequip = False

    # ITEM OPERATIONS
    def set_equipment_details(self):
        collection_data = collections[self.equipment_collection]
        type_data = types[self.equipment_type]
        class_data = classes[type_data['info']['class']]

        equipment_id = class_data['id'] + type_data['id'] + collection_data['id']

        equipment_info = {
            'name': ' '.join([json_dict['info']['name'] for json_dict in [collection_data, type_data]]),
            'class': class_data['info']['class'],
            'type': self.equipment_type,
            'is_magical': type_data['info']['is_magical'],
            'value': int(math.prod([json_dict['info']['value'] for json_dict in [class_data, type_data, collection_data]]))
        }

        equipment_stats = {
            attr: sum([json_dict['stats'][attr] for json_dict in [class_data, type_data, collection_data]])
            for attr in ['attack', 'defence', 'magic', 'agility']
        }

        return equipment_id, equipment_info, equipment_stats

    def equip_status(self,
                     equip: bool):
        self.is_equipped = equip
        self.menu_unequip = equip
        self.menu_equip = 1 - self.menu_unequip

    def equip_item(self,
                   character,
                   equip: bool):
        item_class = self.info['class']
        getattr(character, item_class).equip_status(False) if getattr(character, item_class) else None
        setattr(character, item_class, self)
        self.equip_status(equip)

    # PLAYER ACTIONS
    def set_actions(self):
        """set possible actions for the current item"""
        self.actions.set_actions(self)

    def perform_action(self,
                       interface,
                       key_input: str):
        """perform requested action in the Cell"""
        action_buttons = self.actions.actions_buttons
        key_input = key_input.lower()

        if key_input in action_buttons:
            # equip item
            if key_input == 'e':
                self.equip_item(interface.player, True)

            elif key_input == 'u':
                self.equip_item(interface.player, False)
            
            else:
                kwargs = {'target_object': self,
                          'interface': interface}
                # generic actions
                self.actions.perform_action(key_input, **kwargs)
        else:
            print("""Invalid Entry""")
            pass
