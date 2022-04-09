import os
from tabulate import tabulate

from src.classes.actions import ActionSet


class Equipment:
    def __init__(self,
                 equipment_dict: dict):
        self.hash = hash(self)
        self.id = equipment_dict['item_id']
        self.info = equipment_dict['info']
        self.stats = equipment_dict['stats']
        self.is_equipped = False

        self.actions = ActionSet()
        self.menu_back = True
        self.menu_equip = True
        self.menu_unequip = False

    # ITEM OPERATIONS
    def print(self):
        os.system('clear')
        print(tabulate([row for row in (self.info | self.stats).items()], headers=['key', 'value']))

    def equip_status(self,
                     equip: bool):
        self.is_equipped = equip
        self.menu_unequip = equip
        self.menu_equip = 1 - self.menu_unequip

    def equip_item(self,
                   player,
                   equip: bool):
        item_class = player.selected_item.info['class']
        getattr(player, item_class).equip_status(False) if getattr(player, item_class) else None
        setattr(player, item_class, self)
        self.equip_status(equip)
        player.path_to_screen.pop()
        player.current_screen = player.path_to_screen[-1]
        player.player_inventory.set_equipment_stats()

    # PLAYER ACTIONS
    def set_actions(self):
        """set possible actions for the current item"""
        self.actions.set_actions(self)

    def perform_action(self,
                       player,
                       key_input: str):
        """perform requested action in the Cell"""
        action_buttons = self.actions.actions_buttons
        key_input = key_input.lower()

        if key_input in action_buttons:
            # equip item
            if key_input == 'e':
                self.equip_item(player, True)

            if key_input == 'u':
                self.equip_item(player, False)

            # back
            elif key_input == 'b':
                player.path_to_screen.pop()
                player.current_screen = player.path_to_screen[-1]
        else:
            print("""Invalid Entry""")
            pass
