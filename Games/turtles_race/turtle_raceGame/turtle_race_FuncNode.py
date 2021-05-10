from structures.func_Node import FuncNode
from Games.turtles_race.turtle_raceGame.turtle_race_script import TurtleRace
from structures.game_class import Game


def func():
    game = TurtleRace()

    def inner():
        Game.start_game(game)

    return inner()


TurtleRace_FuncNode = FuncNode("Play", func)
