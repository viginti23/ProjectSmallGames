from structures.menu_Node import MenuNode
from mainMenuForUsers.myAccount.my_Account import MyAccount
from mainMenuForUsers.Logout.logout_FuncNode import logOut_FuncNode
# from MyBest import MyBest
from mainMenuForUsers.chooseGame.chooseGameMenu import chooseGame_Menu


content = {}
options = [chooseGame_Menu, MyAccount, logOut_FuncNode]

MainMenuForUsers = MenuNode("User's Main Menu", content, main_menu=True, options=options)
MenuNode.default_node = MainMenuForUsers
