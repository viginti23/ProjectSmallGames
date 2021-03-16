from structures.user_class import User
from structures.menu_Node import MenuNode
from json_data_funcs import read_data_from_users_database, write_data_to_users_database
import time


def wallet_refill():
    users = read_data_from_users_database()
    player = User.user_logged
    req = player.create_refill_request()
    print('0')
    player.send_refill_request_to_admins(req)
    print('1')

    usr_dict = player.__dict__
    print('2')
    print('3')
    for u in users['users']:
        if u['username'] == usr_dict['username']:
            del u
    users['users'].append(usr_dict)
    print('tut')
    write_data_to_users_database(users)
    print('tuta')
    time.sleep(3)
    MenuNode.current_node()

