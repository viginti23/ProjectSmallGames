from menuNode import MenuNode
from Games.coin_flip.coin_flipMenu import CoinFlip

choose_game = {}

chooseGameMenu = MenuNode("Choose game", choose_game)
chooseGameMenu.add_options(CoinFlip)

