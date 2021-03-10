from structures.menu_Node import MenuNode
from myWallet import MyWallet


my_account = {}

MyAccount = MenuNode("My Account", my_account)
MyAccount.add_options(MyWallet)
# MyAccount()
# My Wallet -> Charge wallet -> request to admin