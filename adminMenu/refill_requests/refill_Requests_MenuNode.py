from structures.menu_Node import MenuNode
from adminMenu.refill_requests.print_Requests_FuncNode import print_refill_requests

content = {}

refillRequests = MenuNode("Refill requests", content)
refillRequests.add_options(print_refill_requests)
