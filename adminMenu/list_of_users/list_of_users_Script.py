import json_data_funcs
from structures.menu_Node import MenuNode


def list_users():
    users = json_data_funcs.read_data_from_users_database()
    if len(users['users']) == 0:
        print("\nThere are no users yet!\n")
    n = 1
    for user in users['users']:
        print(f"\n----->|{n}| {user['username']} ----- {user['email']}\n----------> Wallet status: {user['wallet']}\n\n")
        n += 1
    inp = input("Press enter to go back.")
    return MenuNode.current_node()
