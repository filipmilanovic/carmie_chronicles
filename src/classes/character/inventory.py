import json

from classes.shared.action import ActionSet
from classes.item.equipment import Equipment
from gui.inventory import GUIInventory

from functions.action import quit_action

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

    # INVENTORY OPERATIONS
    def add_item(self,
                 character,
                 item,
                 equip=False):
        self.items.append(item)
        self.menu_pages = 1 + len(self.items) // 9

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

        if key_input in action_buttons:
            # item selection
            if key_input.isnumeric():
                self.selected_item = self.items[int(key_input) - 1 + 9 * self.menu_page]
                interface.path_to_screen.append(self.selected_item)
                interface.current_screen = self.selected_item

            elif key_input == '.':
                self.menu_page = self.menu_page + 1
                self.menu_pages_after = False if self.menu_page == self.menu_pages - 1 else True
                self.menu_pages_before = True

            elif key_input == ',':
                self.menu_page = self.menu_page - 1
                self.menu_pages_before = False if self.menu_page == 0 else True
                self.menu_pages_after = True

            elif key_input == 'e':
                print(self.equipment_stats)

            # back
            elif key_input == 'b':
                interface.path_to_screen.pop()
                interface.current_screen = interface.path_to_screen[-1]

            # quit
            elif key_input == 'q':
                quit_action()
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