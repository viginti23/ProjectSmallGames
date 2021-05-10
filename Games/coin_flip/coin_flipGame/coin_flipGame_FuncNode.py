from structures.func_Node import FuncNode
from Games.coin_flip.coin_flipGame.coin_flipGame_script import CoinF
from structures.game_class import Game


def func():
    game = CoinF()

    def inner():
        Game.start_game(game)

    return inner()



coin_flipFuncNode = FuncNode("Play", func)
