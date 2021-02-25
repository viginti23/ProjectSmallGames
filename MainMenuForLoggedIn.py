from Node import Node
from StartGameMenu import StartGameMenu
from RegisterMenu import RegisterMenu
from LoginMenu import LoginMenu
from BestScores import BestScores

main_menu = {
    1: '|1| Play',
    2: '|2| My account',
    3: '|3| Register',
    4: '|4| Best scores',
}

MainMenu = Node("MainMenu", main_menu)
MainMenu.add_options(StartGameMenu, RegisterMenu, LoginMenu, BestScores
                     ) #wymieniamy które z modułów chcemy mieć dostępne w danym view

