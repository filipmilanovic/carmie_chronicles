import os

from classes.shared.interface import Interface

os.system('clear')

game = Interface()
game.generate_map(rows=5,
                  cols=5,
                  towns=2)
game.generate_player()

while True:
    game.get_actions()
    x = input()
    os.system('clear')
    game.perform_action(x)
