from structures.menu_Node import MenuNode
from Games.turtles_race.turtle_raceGame.turtle_race_FuncNode import TurtleRace_FuncNode
from Games.turtles_race.turtle_raceBestScores.turtle_raceBestScores_FuncNode import turtle_raceBestScores

content = {}
options = [TurtleRace_FuncNode, turtle_raceBestScores]


TurtleRace_Menu = MenuNode("Turtle Race", content, options=options)
