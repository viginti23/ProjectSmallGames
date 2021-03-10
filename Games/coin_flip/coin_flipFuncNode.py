from Structures.funcNode import FuncNode
from Games.coin_flip import coin_flipMenu
# import Games.coin_flip.coin_flipScript
from Games.coin_flip.coin_flipScript import start

func = start
CoinFlipFunc = FuncNode("Play", func, parent_up_menu=coin_flipMenu)
