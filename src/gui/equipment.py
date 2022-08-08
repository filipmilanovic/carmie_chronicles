from tabulate import tabulate

from classes.shared.gui import GUI

class GUIEquipment(GUI):
    def __init__(self,
                 item):
        self.item = item

    def print_screen(self):
        info = self.item.info
        stats = self.item.stats

        print(tabulate([row for row in (info | stats).items()], headers=['key', 'value']))
