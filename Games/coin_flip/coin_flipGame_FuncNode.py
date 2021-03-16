from structures.func_Node import FuncNode
from Games.coin_flip.coin_flipGame_script import CoinF
from structures.game_class import Game

game = CoinF()
func = game.start_game

coin_flipGame = FuncNode("Play", func)
Game.games_list.append(coin_flipGame)

