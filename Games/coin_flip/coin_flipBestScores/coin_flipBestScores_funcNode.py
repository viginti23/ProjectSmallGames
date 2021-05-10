from structures.func_Node import FuncNode
from structures.game_class import Game


def return_func():
    gamename = "Coin Flip"

    def wrapper():
        Game.display_top_n(gamename)

    wrapper()
    return wrapper()


func = return_func

coinFlipBestScores = FuncNode("Coin Flip Records", func)
