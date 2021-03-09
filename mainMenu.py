from menuNode import MenuNode
from registerMenu import RegisterMenu
from loginMenu import LoginMenu
from best_scores import BestScores
from playAsGuest import PlayAsAGuest

main_menu = {}

MainMenu = MenuNode("Main Menu", main_menu)
MainMenu.add_options(PlayAsAGuest, LoginMenu, RegisterMenu, BestScores)
MenuNode.default_node = MainMenu
MenuNode.current_node = MainMenu
MainMenu()
