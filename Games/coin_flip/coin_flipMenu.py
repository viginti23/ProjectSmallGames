from structures.menu_Node import MenuNode
from Games.coin_flip.coin_flipGame.coin_flipGame_FuncNode import coin_flipFuncNode
from Games.coin_flip.coin_flipBestScores.coin_flipBestScores_funcNode import coinFlipBestScores

content = {}
options = [coin_flipFuncNode, coinFlipBestScores]
CoinFlip = MenuNode("Coin Flip", content, options=options)
