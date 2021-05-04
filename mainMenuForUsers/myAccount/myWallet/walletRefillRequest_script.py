from structures.user_class import User
from structures.Refill_Requests import RefRequest
from structures.menu_Node import MenuNode
import time


def wallet_refill():

    # player = User.logged
    # usr_dict = player.__dict__
    req = RefRequest()
    req.save_request_in_reqs_box()
    time.sleep(3)
    return MenuNode.current_node()

