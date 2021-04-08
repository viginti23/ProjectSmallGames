from structures.menu_Node import MenuNode
from adminMenu.refill_requests.show_all_Requests_FuncNode import show_reqs_FuncNode
content = {}
options = [show_reqs_FuncNode]

refillRequests_MenuNode = MenuNode("Refill requests", content, options=options)
