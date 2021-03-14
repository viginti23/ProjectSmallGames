from guestMenu.Login.loginMenu import LoginMenu
from guestMenu.Register.registerFuncNode import RegisterMenu
from guestMenu.bestScores.best_scores import BestScores
from guestMenu.playAsGuest.playAsGuestMenu import PlayAsAGuest
from structures.menu_Node import MenuNode

main_menu = {}

MainMenu = MenuNode("Main Menu", main_menu)
MainMenu.add_options(PlayAsAGuest, LoginMenu, RegisterMenu, BestScores)
MenuNode.default_node = MainMenu
MenuNode.current_node = MainMenu
