import json_data_funcs
from Games.coin_flip.coin_flipGame_script import CoinF
from structures.menu_Node import MenuNode


def show():
    try:
        top5 = json_data_funcs.read_data_from_games_database()['games']["Coin FLip"]['top5']
        t = top5.sort(key=lambda x: x["Wins strike"])
        c = 1
        for result in t:
            print(f'|{c}| {result}')
            c += 1
    except TypeError:
        print("\nThere are no records yet!\n")

    p = input("\nEnter any key to go back.\n")
    MenuNode.current_node()



