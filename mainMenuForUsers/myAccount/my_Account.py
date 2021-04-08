from structures.menu_Node import MenuNode
from mainMenuForUsers.myAccount.myWallet.myWallet import MyWallet
from mainMenuForUsers.myAccount.myBest import MyBest
my_account = {}
options = [MyWallet, MyBest]

MyAccount = MenuNode("My Account", my_account, options=options)
