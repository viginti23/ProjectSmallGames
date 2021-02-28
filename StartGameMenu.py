from MenuNode import MenuNode

start_game = {
    '1': '|1| Game 1',
    '2': '|2| Game 2',
    '3': '|3| Game 3'
}

StartGameMenu = MenuNode("StartGameMenu", start_game)


# w start_game można mieć inne skrypty (gra, dalsze menu, formularz)
# pamiętać o zatrzymaniu breakiem pętli while ze skryptu wyżej