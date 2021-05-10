from structures.menu_Node import MenuNode
from adminMenu.refill_requests.refill_Requests_FuncNode import refillRequests_FuncNode
from mainMenuForUsers.Logout.logout_FuncNode import logOut_FuncNode
from adminMenu.total_register.total_registerFuncNode import total_system_register
from adminMenu.list_of_users.list_of_users_FuncNode import list_of_users_FuncNode
content = {}
options = [refillRequests_FuncNode, list_of_users_FuncNode, total_system_register, logOut_FuncNode]
admin_Menu = MenuNode("Admin menu", content, main_menu=True, options=options)
MenuNode.default_node = admin_Menu
