from Structures.menuNode import MenuNode
from mainMenuForUsers.chooseGame.chooseGameMenu import chooseGameMenu
# from MyAccount import MyAccount
# from LogOut import LogOut
# from MyBest import MyBest


main_menu_for_logged_in = {}

MainMenuForUsers = MenuNode("Main mainMenuForUsers For Users", main_menu_for_logged_in)
MainMenuForUsers.add_options(chooseGameMenu)