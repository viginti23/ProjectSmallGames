from structures.func_Node import FuncNode
from guestMenu.Register.registerScript import RegisterScript


func = RegisterScript.register_script
RegisterMenu = FuncNode("Register", func)
RegisterMenu.parent_up = FuncNode.default_node
