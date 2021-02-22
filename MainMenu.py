from Node import Node
from StartGameMenu import StartGameMenu
from RegisterMenu import RegisterMenu
from LoginMenu import LoginMenu

main_menu = {
    1: '|1| Start game',
    2: '|2| Register',
    3: '|3| Log in',
}

MainMenu = Node("MainMenu", main_menu)
MainMenu.add_options(StartGameMenu, RegisterMenu, LoginMenu) #wymieniamy które z modułów chcemy mieć dostępne w danym view

