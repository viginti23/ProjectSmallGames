class Game:
    def __init__(self):
        self.name = "stan"
    def start_game(self):
        return 3

game = Game()

func = game.start_game

for f in dir(func):
    print(f)

