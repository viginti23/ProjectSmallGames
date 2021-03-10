from structures.menu_Node import MenuNode
from Games.coin_flip.coin_flipMenu import CoinFlip

choose_game = {}

ChooseGameMenu = MenuNode("Choose game", choose_game)
ChooseGameMenu.add_options(CoinFlip)

