import json

from classes.shared.action import ActionSet

from gui.attributes import GUIAttributes

from functions.action import back_action, quit_action

with open('src/dicts/attribute.json', 'r') as file:
    attributes = json.load(file)

class Attributes:
    def __init__(self):
        self.hash = hash(self)
        self.gui = GUIAttributes(self)
        self.actions = ActionSet()

        self.set_default_attributes()

        self.menu_back = True
    
    def set_default_attributes(self):
        [setattr(self, attr['name'], attr['default']) for attr in attributes.values()]
    
    def set_actions(self):
        """set possible actions for the current Cell"""
        self.actions.set_actions(self)
    
    def perform_action(self,
                       interface,
                       key_input: str):
        # back
        if key_input == 'b':
            back_action(interface)

        # quit
        elif key_input == 'q':
            quit_action()
