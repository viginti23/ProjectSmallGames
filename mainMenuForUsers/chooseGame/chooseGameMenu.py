from structures.menu_Node import MenuNode
from Games.coin_flip.coin_flipMenu import CoinFlip
from Games.turtles_race.turtle_raceMenu import TurtleRace_Menu
import structures.user_class as uc
from importlib import reload

choose_game = {}

name = "Choose game"

options = [CoinFlip, TurtleRace_Menu]

chooseGame_Menu = MenuNode(name, choose_game, options=options)

# if not MenuNode.check_logged_user():
#     chooseGame_Menu.name = "PLay as guest"
