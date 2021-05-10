import json_data_funcs
from structures.func_Node import FuncNode
from structures.game_class import Game


def return_funcTurtle():
    gamename = "Turtle Race"

    def wrapper():
        Game.display_personal_best(gamename)

    return wrapper()


func1 = return_funcTurtle
my_bestCoinFlip = FuncNode("Turtle Race", func=func1)


def return_funcCoinFlip():
    gamename = "Coin Flip"

    def wrapper():
        Game.display_personal_best(gamename)

    return wrapper()


func2 = return_funcCoinFlip
my_bestTurtleRace = FuncNode("Coin Flip", func=func2)
