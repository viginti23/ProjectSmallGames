from structures.menu_Node import MenuNode
from mainMenuForUsers.myAccount.myWallet.walletStatus import walletStatus
from mainMenuForUsers.myAccount.myWallet.walletRefillRequest import walletRefillRequest
my_wallet = {}
options = [walletStatus, walletRefillRequest]

MyWallet = MenuNode("My Wallet", my_wallet, options=options)

