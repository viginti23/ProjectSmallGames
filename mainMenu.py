from MenuNode import MenuNode
from RegisterMenu import RegisterMenu
from loginMenu import LoginMenu
from best_scores import BestScores
from PlayAsAGuest import PlayAsAGuest

main_menu = {}

MainMenu = MenuNode("Main Menu", main_menu)
MainMenu.add_options(PlayAsAGuest, LoginMenu, RegisterMenu, BestScores)
MenuNode.default_node = MainMenu
MainMenu()
