import os
print(os.getcwd())

import json

with open('src/dicts/controls.json', 'r') as file:
    controls = json.load(file)


class ActionSet:
    def __init__(self):
        self.hash = hash(self)
        self.action_type = None
        self.actions_buttons = None
        self.actions_display = None

    def get_valid_actions(self,
                          target_object,
                          input_dict: dict,
                          output: str):
        """get the valid actions for the screen given the current attributes of the screen"""
        actions = input_dict.values()
        return [action.get(output) for action in actions
                if target_object.__dict__.get(action.get('requirement', 'hash'))]

    def set_actions(self,
                    target_object):
        """generate allowed key-presses to send to the Player, as well as the display for the interface"""
        valid_buttons = self.get_valid_actions(target_object, controls, 'button')
        valid_display = self.get_valid_actions(target_object, controls, 'display')

        self.actions_buttons = valid_buttons
        self.actions_display = ', '.join(valid_display)
