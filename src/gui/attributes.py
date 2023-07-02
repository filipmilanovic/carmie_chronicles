from classes.shared.gui import GUI

class GUIAttributes(GUI):
    def __init__(self,
                 attributes):
        self.attributes = attributes
        
    def print_screen(self):
        print(self.attributes.__dict__)
