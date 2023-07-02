import yaml

from classes.shared.action import ActionSet

with open('src/dicts/control.yaml', 'r') as file:
    controls = yaml.safe_load(file)
map_cell_dict = {}


class Cell:
    """a Cell class object denoting one region on the Map"""
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
        self.menu_inventory = True
        self.menu_attributes = True

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
        key_input = key_input.lower()

        if key_input in self.actions.actions_buttons:
            if key_input in ('w', 'a', 's', 'd'):
                # movement
                direction = [action['requirement'] for action in controls.values() if action['button'] == key_input][0]
                new_location_hash = self.__dict__[direction]
                if new_location_hash:
                    self.update_appearance(False)
                    interface.map.current_cell = map_cell_dict[new_location_hash]
                    interface.map.current_cell.update_appearance(True)
                    interface.map.generate_grid()
            else:
                kwargs = {'target_object': self,
                          'interface': interface}
                # generic actions
                self.actions.perform_action(key_input, **kwargs)
        
        else:
            print("""Invalid Entry""")
            pass
