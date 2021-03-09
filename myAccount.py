import json
from user import User
from menuNode import MenuNode

my_account = {}

MyAccount = MenuNode("My Account", my_account, parent=MenuNode.default_node)
# MyAccount.add_options()
# MyAccount()
# My Wallet -> Charge wallet -> request to admin