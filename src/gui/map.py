from classes.shared.gui import GUI

class GUIMap(GUI):
    def __init__(self,
                 map):
        self.map = map
        
    def print_screen(self):
        print(self.map.grid)
