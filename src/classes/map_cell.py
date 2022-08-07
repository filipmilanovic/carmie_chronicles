import json

from classes.action import ActionSet
from functions.action import quit_action

with open('src/dicts/control.json', 'r') as file:
    controls = json.load(file)

map_cell_dict = {}


class MapCell:
    """a MapCell class object denoting one region on the Map"""
    instances = []

    def __init__(self):
        self.hash = hash(self)
        map_cell_dict[self.hash] = self
        self.is_player_cell = False
        self.appearance = 'o'
        self.north_hash = None
        self.west_hash = None
        self.south_hash = None
        self.east_hash = None
        self.is_town = None

        self.actions = ActionSet()
        self.menu_items = True

    # CELL OPERATIONS
    def update_appearance(self,
                          is_player_cell: bool):
        """set the appearance of the Cell in the Map given its attributes and the Player's location"""
        self.is_player_cell = is_player_cell

        if self.is_player_cell:
            self.appearance = 'x'
        elif self.is_town:
            self.appearance = 't'
        else:
            self.appearance = 'o'

    # PLAYER ACTIONS
    def set_actions(self):
        """set possible actions for the current Cell"""
        self.actions.set_actions(self)

    def perform_action(self,
                       interface,
                       key_input: str):
        """perform requested action in the Cell"""
        action_buttons = self.actions.actions_buttons
        key_input = key_input.lower()

        if key_input in action_buttons:
            # directions
            if key_input in ('w', 'a', 's', 'd'):
                direction = [action['requirement'] for action in controls.values() if action['button'] == key_input][0]
                new_location_hash = self.__dict__[direction]
                if new_location_hash:
                    self.update_appearance(False)
                    interface.current_cell = map_cell_dict[new_location_hash]
                    interface.current_cell.update_appearance(True)
                    interface.map.generate_grid()

            # inventory
            elif key_input == 'i':
                interface.current_screen = interface.player.player_inventory
                interface.path_to_screen.append(interface.player.player_inventory)

            # trade
            elif key_input == 't':
                print('Trade not currently available')

            # quit
            elif key_input == 'q':
                quit_action()
        else:
            print("""Invalid Entry""")
            pass
