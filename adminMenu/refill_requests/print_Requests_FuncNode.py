from structures.func_Node import FuncNode
from structures.user_class import User, Admin

adm = User.user_logged

func = adm.requests_queue()

print_refill_requests = FuncNode("Show requests", func)
