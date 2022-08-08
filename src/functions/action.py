def attributes_action(interface):
    interface.current_screen = interface.player.attributes
    interface.path_to_screen.append(interface.player.attributes)


def back_action(interface):
    interface.path_to_screen.pop()
    interface.current_screen = interface.path_to_screen[-1]


def inventory_action(interface):
    interface.current_screen = interface.player.inventory
    interface.path_to_screen.append(interface.player.inventory)


def quit_action():
    print('Thanks for playing!')
    quit()


def trade_action(interface):
    print('Trade not currently available')
