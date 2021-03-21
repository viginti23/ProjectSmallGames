import json_data_funcs
from structures.menu_Node import MenuNode


def show():
    try:
        games = json_data_funcs.read_data_from_games_database()
        top5 = games['games']["Coin FLip"]['top5']
        t = top5.sort(key=lambda x: x["Wins strike"])
        c = 1
        for result in t:
            print(f'|{c}| {result}')
            c += 1
    except TypeError:
        print("\nThere are no records yet!\n")

    p = input("\nEnter any key to go back.\n")
    return MenuNode.current_node()



