from Structures.menuNode import MenuNode
from mainMenuForUsers.myAccount.myWallet import MyWallet


my_account = {}

MyAccount = MenuNode("My Account", my_account, parent=MenuNode.default_node)
MyAccount.add_options(MyWallet)
# MyAccount()
# My Wallet -> Charge wallet -> request to admin