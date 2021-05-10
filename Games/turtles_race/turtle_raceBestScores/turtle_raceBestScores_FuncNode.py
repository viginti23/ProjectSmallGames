from structures.func_Node import FuncNode
from structures.game_class import Game

from structures.func_Node import FuncNode
from structures.game_class import Game


def return_func():
    gamename = "Turtle Race"

    def wrapper():
        Game.display_top_n(gamename)

    return wrapper()


func = return_func

turtle_raceBestScores = FuncNode("Turtle Race Records", func)
