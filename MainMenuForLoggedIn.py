from MenuNode import MenuNode
from StartGameMenu import StartGameMenu
from RegisterMenu import RegisterMenu
from LoginMenu import LoginMenu
from BestScores import BestScores
from LogOut import LogOut


main_menu = {}

MainMenuForLoggedIn = MenuNode("MainMenuForLoggedIn", main_menu)
MainMenuForLoggedIn.add_options(StartGameMenu, RegisterMenu, LoginMenu, BestScores)
