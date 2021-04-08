from structures.menu_Node import MenuNode
from adminMenu.refill_requests.refill_Requests_MenuNode import refillRequests_MenuNode
from mainMenuForUsers.Logout.logout_FuncNode import logOut_FuncNode
content = {}
options = [refillRequests_MenuNode, logOut_FuncNode]

admin_Menu = MenuNode("Admin menu", content, main_menu=True, options=options)
MenuNode.default_node = admin_Menu
