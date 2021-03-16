import json_data_funcs
from structures.user_class import User
from structures.menu_Node import MenuNode


def list_users():
    users = json_data_funcs.read_data_from_users_database()
    for user in users['users']:
        print(
            f"""\n-----> {user['username']}
            ----------> {user['wallet']}
""")
    inp = input("Press enter to go back.")
    MenuNode.current_node()
