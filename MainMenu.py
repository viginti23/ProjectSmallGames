from Node import Node
from StartGameMenu import StartGameMenu
from RegisterMenu import RegisterMenu
from LoginMenu import LoginMenu

main_menu = {
    1: '|1| Play as guest',
    2: '|2| Log in',
    3: '|3| Register',
}

MainMenu = Node("MainMenu", main_menu)
MainMenu.add_options(StartGameMenu, RegisterMenu, LoginMenu) #wymieniamy które z modułów chcemy mieć dostępne w danym view

