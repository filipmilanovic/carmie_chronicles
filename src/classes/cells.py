import json

from src.classes.actions import ActionSet

with open('../src/dicts/controls.json', 'r') as file:
    controls = json.load(file)

cell_dict = {}


class Cell:
    """a Cell class object denoting one region on the Map"""
    instances = []

    def __init__(self):
        self.hash = hash(self)
        cell_dict[self.hash] = self
        self.player_cell = False
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
                          player_cell: bool):
        """set the appearance of the Cell in the Map given its attributes and the Player's location"""
        self.player_cell = player_cell

        if self.player_cell:
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
                       player,
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
                    player.current_cell = cell_dict[new_location_hash]
                    player.current_cell.update_appearance(True)
                    player.map.generate_grid()

            # inventory
            elif key_input == 'i':
                player.path_to_screen.append(player.player_inventory)
                player.current_screen = player.player_inventory

            # trade
            elif key_input == 't':
                print('Trade not currently available')

            # quit
            elif key_input == 'q':
                print('Thanks for playing!')
                quit()
        else:
            print("""Invalid Entry""")
            pass
