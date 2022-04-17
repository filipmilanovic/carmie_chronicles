import json
import os
from tabulate import tabulate

from classes.action import ActionSet
from classes.equipment import Equipment
from functions.action import quit_action

with open('src/dicts/attribute.json', 'r') as file:
    attributes = json.load(file)


class PlayerInventory:
    def __init__(self,
                 player):
        self.hash = hash(self)
        self.player = player
        self.items = []

        # EQUIPMENT
        self.equipment_stats = {}

        # SET STARTING EQUIPMENT
        self.add_item(Equipment('dagger', 'basic'), True)
        self.add_item(Equipment('shirt', 'basic'), True)
        self.add_item(Equipment('pants', 'basic'), True)

        # ACTIONS
        self.actions = ActionSet()
        self.menu_pages = len(self.items) // 9 + 1
        self.menu_page = 0
        self.menu_pages_before = False
        self.menu_pages_after = True if len(self.items) > 9 else False

        self.menu_back = True
        self.menu_equip = True

    # INVENTORY OPERATIONS
    def add_item(self,
                 item,
                 equip=False):
        self.items.append(item)
        self.menu_pages = 1 + len(self.items) // 9

        item.equip_item(self.player, equip) if equip else None

    def print(self):
        print_range = range(self.menu_page * 9,
                            (1 + self.menu_page) * 9 if not (self.menu_page == self.menu_pages - 1)
                            else self.menu_page * 9 + len(self.items) % 9)
        print_items = [self.items[i] for i in print_range]

        os.system('clear')
        print(tabulate([[self.items.index(item) + 1 - 9 * self.menu_page,
                         item.info['name'],
                         item.info['class'],
                         item.is_equipped]
                        for item in print_items],
                       headers=['name', 'class', 'equipped']))

    # PLAYER ACTIONS
    def set_actions(self):
        """set possible actions for the current screen"""
        [setattr(self, f'select_{i+1}', self.items[i]) if i < len(self.items) else None for i in range(9)]
        self.actions.set_actions(self)

    def perform_action(self,
                       key_input: str):
        """perform requested action in the Cell"""
        action_buttons = self.actions.actions_buttons
        key_input = key_input.lower()

        if key_input in action_buttons:
            # item selection
            if key_input.isnumeric():
                self.player.selected_item = self.items[int(key_input) - 1 + 9 * self.menu_page]
                self.player.path_to_screen.append(self.player.selected_item)
                self.player.current_screen = self.player.selected_item

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
                self.player.path_to_screen.pop()
                self.player.current_screen = self.player.path_to_screen[-1]

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

#     def show_equipment(self):
#         print(f'''
#            ___      {self.player.head.info['name'] if self.player.head else None}
#           |   |
#           |   |   |
#            ---    | {self.player.weapon.info['name'] if self.player.weapon else None}
#             |     |
#        -----------|
#             |
#             |       {self.player.body.info['name'] if self.player.body else None}
#             |
#            / \\
#           /   \\     {self.player.legs.info['name'] if self.player.legs else None}
#          /     \\
#
# {print(self.equipment_stats)}''')
