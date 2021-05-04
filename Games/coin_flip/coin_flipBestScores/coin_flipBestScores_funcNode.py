from structures.func_Node import FuncNode
from structures.game_class import Game

Game.current_game = "Coin Flip"
func = Game.display_top_n

coinFlipBestScores = FuncNode("Best scores", func)
