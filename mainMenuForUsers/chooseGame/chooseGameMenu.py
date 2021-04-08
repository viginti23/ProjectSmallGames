from structures.menu_Node import MenuNode
from Games.coin_flip.coin_flipMenu import CoinFlip
import structures.user_class as uc
from importlib import reload

choose_game = {}

name = "Choose game"

options = [CoinFlip]

chooseGame_Menu = MenuNode(name, choose_game, options=options)

# if not MenuNode.check_logged_user():
#     chooseGame_Menu.name = "PLay as guest"
