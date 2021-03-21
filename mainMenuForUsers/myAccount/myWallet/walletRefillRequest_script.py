from structures.user_class import User
from structures.menu_Node import MenuNode
from json_data_funcs import read_data_from_users_database, write_data_to_users_database
import time


def wallet_refill():

    player = User.logged
    usr_dict = player.__dict__

    req = player.create_refill_request()
    # print('0')
    player.send_refill_request_to_admins(req)
    # print('1')
    # print('tut')
    # print('tuta')
    time.sleep(5)
    return MenuNode.current_node()

# wallet_refill()
