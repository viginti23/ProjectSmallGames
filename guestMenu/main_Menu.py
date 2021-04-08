from guestMenu.Login.loginFuncNode import login_FuncNode
from guestMenu.Register.registerFuncNode import RegisterMenu
from guestMenu.bestScores.best_scores import BestScores
from mainMenuForUsers.chooseGame.chooseGameMenu import chooseGame_Menu
from structures.menu_Node import MenuNode

content = {}

options = [chooseGame_Menu, login_FuncNode, RegisterMenu, BestScores]

MainMenu = MenuNode("Main Menu", content, main_menu=True, options=options)

MenuNode.current_node = MainMenu
MenuNode.default_node = MainMenu
