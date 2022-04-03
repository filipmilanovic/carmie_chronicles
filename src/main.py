from classes.interface import Interface

game = Interface()
game.generate_map(rows=5,
                  cols=5,
                  towns=2)
game.generate_player()

while True:
    print(game.get_actions())
    x = input()
    game.player.actions.actions_map(x)
