from MenuNode import MenuNode
from StartGameMenu import StartGameMenu
from RegisterMenu import RegisterMenu
from LoginMenu import LoginMenu
from BestScores import BestScores

main_menu = {
    '1': '|1| Play',
    '2': '|2| My account',
    '3': '|4| Best scores',
}

MainMenu = MenuNode("MainMenuForLoggedIn", main_menu)
MainMenu.add_options(StartGameMenu, RegisterMenu, LoginMenu, BestScores)