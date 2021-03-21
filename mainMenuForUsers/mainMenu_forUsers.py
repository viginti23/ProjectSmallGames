from structures.menu_Node import MenuNode
from mainMenuForUsers.chooseGame.chooseGameMenu import ChooseGameMenu
from mainMenuForUsers.myAccount.my_Account import MyAccount
from mainMenuForUsers.Logout.log_Out import LogOut
# from MyBest import MyBest


content = {}

MainMenuForUsers = MenuNode("User's Main Menu", content, main_menu=True)
MainMenuForUsers.add_options(ChooseGameMenu, MyAccount, LogOut)
MenuNode.default_node = MainMenuForUsers
