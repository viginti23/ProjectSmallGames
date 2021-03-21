from guestMenu.Login.loginMenu import LoginMenu
from guestMenu.Register.registerFuncNode import RegisterMenu
from guestMenu.bestScores.best_scores import BestScores
from guestMenu.playAsGuest.playAsGuestMenu import PlayAsAGuest
from structures.menu_Node import MenuNode

content = {}

MainMenu = MenuNode("Main Menu", content, main_menu=True)
MainMenu.add_options(PlayAsAGuest, LoginMenu, RegisterMenu, BestScores)
MenuNode.current_node = MainMenu
MenuNode.default_node = MainMenu
