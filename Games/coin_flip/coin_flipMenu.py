from structures.menu_Node import MenuNode
from Games.coin_flip.coin_flipGame_FuncNode import coin_flipGame
from Games.coin_flip.coin_flipBestScores_funcNode import coinFlipBestScores

content = {}

CoinFlip = MenuNode("Coin Flip", content)
CoinFlip.add_options(coin_flipGame, coinFlipBestScores)
