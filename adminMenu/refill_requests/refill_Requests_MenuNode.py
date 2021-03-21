from structures.menu_Node import MenuNode
# from adminMenu.refill_requests.one_by_one_FuncNode import one_by_1_FuncNode
from adminMenu.refill_requests.show_all_Requests_FuncNode import show_reqs_FuncNode

content = {}

refillRequests_MenuNode = MenuNode("Refill requests", content)

refillRequests_MenuNode.add_options(show_reqs_FuncNode)
