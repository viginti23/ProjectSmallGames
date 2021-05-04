from structures.menu_Node import MenuNode
from Games.turtles_race.turtle_raceBestScores.turtle_raceBestScores_FuncNode import turtle_raceBestScores
from Games.coin_flip.coin_flipBestScores.coin_flipBestScores_funcNode import coinFlipBestScores


best_scores = {}
options = [coinFlipBestScores, turtle_raceBestScores]
BestScores = MenuNode("Best Scores", best_scores, options=options)
