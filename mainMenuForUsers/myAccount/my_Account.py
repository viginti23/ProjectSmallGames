from structures.menu_Node import MenuNode
from mainMenuForUsers.myAccount.myWallet.myWallet import MyWallet

my_account = {}

MyAccount = MenuNode("My Account", my_account)
MyAccount.add_options(MyWallet)
# MyAccount()
# My Wallet -> Charge wallet -> srequest to admin
