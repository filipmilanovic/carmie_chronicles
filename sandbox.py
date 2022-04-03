import json
from classes.equipment import Equipment

with open('dicts/controls.json', 'r') as file:
    controls = json.load(file)

key_input = 's'
key_dict = {'south_hash': 'test'}
print(controls.values())

print([action['requirement'] for action in controls.values() if action['button'] == 's'][0])

# [print(item) for item in weapons.values() if item['item_id'] in [1000]]
# item = Equipment(weapon['dagger'])
# print(item.__dict__['stats'])
# [print(item.__dict__['stats'][attribute]) for attribute in item.stats]
