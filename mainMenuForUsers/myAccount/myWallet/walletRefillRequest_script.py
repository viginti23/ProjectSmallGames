from structures.user_class import User
from structures.Refill_Requests import RefRequest
from structures.menu_Node import MenuNode
import time


def wallet_refill():

    player = User.logged
    # usr_dict = player.__dict__
    req = RefRequest.create_refill_request(player)
    RefRequest.send_refill_request_to_admins(player, req)
    time.sleep(5)
    return MenuNode.current_node()

