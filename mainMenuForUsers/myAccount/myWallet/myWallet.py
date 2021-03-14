from structures.menu_Node import MenuNode
from mainMenuForUsers.myAccount.myWallet.walletStatus import walletStatus
from mainMenuForUsers.myAccount.myWallet.walletRefillRequest import walletRefillRequest
my_wallet = {}

MyWallet = MenuNode("My Wallet", my_wallet)
MyWallet.add_options(walletStatus, walletRefillRequest)
