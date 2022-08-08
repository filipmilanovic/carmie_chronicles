import json

with open('src/dicts/attribute.json', 'r') as file:
    attributes = json.load(file)

class Attributes:
    def __init__(self):
        self.hash = hash(self)
        self.set_default_attributes()
    
    def set_default_attributes(self):
        [setattr(self, attr['name'], attr['default']) for attr in attributes.values()]
