from menuNode import MenuNode
from Games.coin_flip.coin_flipFuncNode import CoinFlipFunc

content = {}

CoinFlip = MenuNode("Coin Flip", content)
CoinFlip.add_options(CoinFlipFunc)
