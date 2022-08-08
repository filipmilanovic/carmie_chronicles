from tabulate import tabulate

from classes.shared.gui import GUI

class GUIInventory(GUI):
    def __init__(self,
                 inventory):
        self.inventory = inventory

    def print_screen(self):
        menu_page = self.inventory.menu_page
        menu_pages = self.inventory.menu_pages
        items = self.inventory.items

        print_range = range(menu_page * 9,
                            (1 + menu_page) * 9 if not (menu_page == menu_pages - 1)
                            else menu_page * 9 + len(items) % 9)
        print_items = [items[i] for i in print_range]

        print(tabulate([[items.index(item) + 1 - 9 * menu_page,
                         item.info['name'],
                         item.info['class'],
                         item.is_equipped]
                        for item in print_items],
                       headers=['name', 'class', 'equipped']))
