from structures.user_class import User
from structures.menu_Node import MenuNode
from json_data_funcs import read_data_from_users_database, write_data_to_users_database


def wallet_refill():
    users = read_data_from_users_database()
    player: User = User.user_logged
    req = player.create_refill_request()
    player.send_refill_request_to_admins(req)
    usr_dict = player.__dict__
    users['users'].append(usr_dict)

    for u in users['users']:
        if u['username'] == player.username:
            del u
            users['users'].append(usr_dict)

    write_data_to_users_database(users)

    MenuNode.current_node()
