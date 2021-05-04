from structures.menu_Node import MenuNode
from mainMenuForUsers.myAccount.myWallet.myWallet import MyWallet
from mainMenuForUsers.myAccount.myBest.myBest_MenuNode import myBest_MenuNode

my_account = {}
options = [MyWallet, myBest_MenuNode]

MyAccount = MenuNode("My Account", my_account, options=options)
