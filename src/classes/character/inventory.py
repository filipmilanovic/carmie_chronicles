import json

from classes.shared.action import ActionSet
from classes.item.equipment import Equipment
from gui.inventory import GUIInventory

with open('src/dicts/attribute.json', 'r') as file:
    attributes = json.load(file)


class Inventory:
    def __init__(self):
        self.hash = hash(self)
        self.gui = GUIInventory(self)
        self.items = []

        # EQUIPMENT
        self.equipment_stats = {}

        # ACTIONS
        self.actions = ActionSet()
        self.selected_item = None
        self.menu_pages = len(self.items) // 9 + 1
        self.menu_page = 0
        self.menu_pages_before = False
        self.menu_pages_after = True if len(self.items) > 9 else False

        self.menu_back = True
        self.menu_attributes = True

    # INVENTORY OPERATIONS
    def add_item(self,
                 character,
                 item,
                 equip=False):
        self.items.append(item)
        self.menu_pages = 1 + len(self.items) // 9
        self.menu_pages_after = True if self.menu_pages > 1 else False

        item.equip_item(character, equip) if equip else None

    # PLAYER ACTIONS
    def set_actions(self):
        """set possible actions for the current screen"""
        [setattr(self, f'select_{i+1}', self.items[i]) if i < len(self.items) else None for i in range(9)]
        self.actions.set_actions(self)

    def perform_action(self,
                       interface,
                       key_input: str):
        """perform requested action in the Cell"""
        action_buttons = self.actions.actions_buttons
        key_input = key_input.lower()

        if key_input in self.actions.actions_buttons:
            if key_input.isnumeric():
                # item selection
                self.selected_item = self.items[int(key_input) - 1 + 9 * self.menu_page]
                interface.path_to_screen.append(self.selected_item)
                interface.current_screen = self.selected_item
            else:
                kwargs = {'target_object': self,
                          'interface': interface}
                # generic actions
                self.actions.perform_action(key_input, **kwargs)
        
        else:
            print("""Invalid Entry""")
            pass

    """EQUIPMENT"""
    def set_equipment_stats(self):
        equipment = [self.player.weapon,
                     self.player.shield,
                     self.player.head,
                     self.player.body,
                     self.player.legs]
        self.equipment_stats = {attr['name']: sum([item.stats[attr['name']] for item in equipment if item])
                                for attr in attributes.values() if attr['equipment']}
