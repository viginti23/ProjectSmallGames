from Structures.menuNode import MenuNode
from mainMenu.Register.registerMenu import RegisterMenu
from mainMenu.Login.loginMenu import LoginMenu
from mainMenu.bestScores.best_scores import BestScores
from mainMenu.playAsGuest.playAsGuest import PlayAsAGuest

main_menu = {}

MainMenu = MenuNode("Main mainMenuForUsers", main_menu)
MainMenu.add_options(PlayAsAGuest, LoginMenu, RegisterMenu, BestScores)
MenuNode.default_node = MainMenu
MenuNode.current_node = MainMenu
MainMenu()
