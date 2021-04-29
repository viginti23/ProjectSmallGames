from structures.func_Node import FuncNode
from Games.turtles_race.turtle_raceGame.turtle_race_script import TurtleRace

t = TurtleRace()
func = t.start_game

TurtleRace_FuncNode = FuncNode("Play", func)
