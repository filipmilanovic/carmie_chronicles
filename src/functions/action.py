def attributes_action(interface):
    interface.current_screen = interface.player.attributes
    interface.path_to_screen.append(interface.player.attributes)


def back_action(interface):
    interface.path_to_screen.pop()
    interface.current_screen = interface.path_to_screen[-1]


def inventory_action(interface):
    interface.current_screen = interface.player.inventory
    interface.path_to_screen.append(interface.player.inventory)


def page_next_action(target_object):
    menu_page = target_object.menu_page
    menu_pages = target_object.menu_pages
    menu_pages_after = target_object.menu_pages_after
    menu_pages_before = target_object.menu_pages_before

    target_object.menu_page = menu_page + 1
    target_object.menu_pages_after = False if menu_page == menu_pages - 1 else True
    target_object.menu_pages_before = True


def page_previous_action(target_object):
    menu_page = target_object.menu_page
    menu_pages_after = target_object.menu_pages_after
    menu_pages_before = target_object.menu_pages_before

    target_object.menu_page = menu_page - 1
    target_object.menu_pages_before = False if menu_page == 0 else True
    target_object.menu_pages_after = True


def quit_action():
    print('Thanks for playing!')
    quit()


def trade_action(interface):
    print('Trade not currently available')
