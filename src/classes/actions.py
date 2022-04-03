import json
from src.classes.cells import cell_dict

with open('../src/dicts/controls.json', 'r') as file:
    controls = json.load(file)


class ActionSet:
    def __init__(self,
                 player):
        self.hash = hash(self)
        self.player = player
        self.action_type = None
        self.actions_buttons = None
        self.actions_display = None

    """GENERAL"""
    def get_valid_actions(self,
                          input_dict: dict,
                          output: str):
        """get the valid actions for the screen given the current attributes of the screen"""
        actions = input_dict.values()
        return [action.get(output) for action in actions if eval(action.get('requirement', 'hash'),
                                                                 self.player.current_cell.__dict__)]

    def set_actions(self):
        """generate allowed key-presses to send to the Player, as well as the display for the interface"""
        valid_buttons = self.get_valid_actions(controls, 'button')
        valid_display = self.get_valid_actions(controls, 'display')

        self.actions_buttons = valid_buttons
        self.actions_display = ', '.join(valid_display)

    """MAP ACTIONS"""
    def actions_map(self,
                    key_input: str):
        """perform requested Player action on the Map"""
        action_buttons = self.actions_buttons
        key_input = key_input.lower()

        if key_input in action_buttons:
            if key_input in ('w', 'a', 's', 'd'):
                direction = [action['requirement'] for action in controls.values() if action['button'] == key_input][0]
                new_location_hash = self.player.current_cell.__dict__[direction]
                if new_location_hash:
                    self.player.current_cell.update_appearance(False)
                    self.player.current_cell = cell_dict[new_location_hash]
                    self.player.current_cell.update_appearance(True)
                    self.player.map.generate_grid()
            elif key_input == 'i':
                self.player.show_inventory()
            elif key_input == 'e':
                self.player.show_equipment()
            elif key_input == 'q':
                print('Thanks for playing!')
                quit()
            self.set_actions()
        else:
            print("""Invalid Entry""")
            pass
