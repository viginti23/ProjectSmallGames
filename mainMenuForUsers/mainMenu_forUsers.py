from structures.menu_Node import MenuNode
from mainMenuForUsers.chooseGame.chooseGameMenu import ChooseGameMenu
from mainMenuForUsers.myAccount.my_Account import MyAccount
# from LogOut import LogOut
# from MyBest import MyBest


main_menu_for_logged_in = {}

MainMenuForUsers = MenuNode("User's Main Menu", main_menu_for_logged_in, main_menu=True)
MainMenuForUsers.add_options(ChooseGameMenu, MyAccount)
