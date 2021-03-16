from structures.menu_Node import MenuNode
from adminMenu.list_of_users.list_of_users_FuncNode import list_of_users_FuncNode

content = {}

admin_Menu = MenuNode("Admin menu", content, main_menu=True)
admin_Menu.add_options(list_of_users_FuncNode)
