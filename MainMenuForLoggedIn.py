from MenuNode import MenuNode
from StartGameMenu import StartGameMenu
# from MyAccount import MyAccount
# from LogOut import LogOut
# from MyBest import MyBest


main_menu_for_logged_in = {}
# add User.user_logged info in every menu for logged user

MainMenuForLoggedIn = MenuNode("Main Menu For Users", main_menu_for_logged_in)
MainMenuForLoggedIn.add_options(StartGameMenu)
