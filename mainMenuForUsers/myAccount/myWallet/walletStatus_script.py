from structures.user_class import User
from structures.menu_Node import MenuNode


def wallet_status():
    user = User.user_logged
    print(f'\nYou have {user.wallet} points in your wallet.\n')
    inp = input("Enter any key to go back.")
    MenuNode.current_node()
