from MenuNode import MenuNode
from RegisterMenu import RegisterMenu
from LoginMenu import LoginMenu
from BestScores import BestScores
from PlayAsAGuest import PlayAsAGuest


main_menu = {}

MainMenu = MenuNode("MainMenu", main_menu)

MainMenu.add_options(PlayAsAGuest, LoginMenu, RegisterMenu, BestScores)

MenuNode.default_node = MainMenu

MainMenu.show_menu_view_and_go_next()

