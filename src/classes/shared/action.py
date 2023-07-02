import yaml

with open('src/dicts/control.yaml', 'r') as file:
    controls = yaml.safe_load(file)


class ActionSet:
    def __init__(self):
        self.hash = hash(self)
        self.actions_buttons = None
        self.actions_display = None
        self.actions_valid = None

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
        valid_actions = self.get_valid_actions(target_object, controls, 'action')

        self.actions_buttons = valid_buttons
        self.actions_display = ', '.join(valid_display)
        self.actions_valid = {valid_buttons[i]: getattr(self, valid_actions[i])
                              for i in range(len(valid_buttons)) if valid_actions[i]}

    def perform_action(self,
                       key_input: str,
                       **kwargs):
        self.actions_valid[key_input](**kwargs)
    
    ## SHARED ACTIONS
    def attributes_action(self,
                          **kwargs):
        interface = kwargs['interface']
        interface.current_screen = interface.player.attributes
        interface.path_to_screen.append(interface.player.attributes)

    def back_action(self,
                    **kwargs):
        interface = kwargs['interface']
        interface.path_to_screen.pop()
        interface.current_screen = interface.path_to_screen[-1]

    def inventory_action(self,
                         **kwargs):  
        interface = kwargs['interface']
        interface.current_screen = interface.player.inventory
        interface.path_to_screen.append(interface.player.inventory)

    def page_next_action(self,
                         **kwargs):
        target_object = kwargs['target_object']
        menu_page = target_object.menu_page
        menu_pages = target_object.menu_pages
        menu_pages_after = target_object.menu_pages_after
        menu_pages_before = target_object.menu_pages_before

        target_object.menu_page = menu_page + 1
        target_object.menu_pages_after = False if menu_page == menu_pages - 1 else True
        target_object.menu_pages_before = True

    def page_previous_action(self,
                             **kwargs):
        target_object = kwargs['target_object']
        menu_page = target_object.menu_page
        menu_pages_after = target_object.menu_pages_after
        menu_pages_before = target_object.menu_pages_before

        target_object.menu_page = menu_page - 1
        target_object.menu_pages_before = False if menu_page == 0 else True
        target_object.menu_pages_after = True

    def quit_action(self,
                    **kwargs):
        print('Thanks for playing!')
        quit()

    def trade_action(self,
                     **kwargs):
        print('Trade not currently available')
