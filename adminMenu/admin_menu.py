from structures.menu_Node import MenuNode
from adminMenu.refill_requests.refill_Requests_MenuNode import refillRequests_MenuNode
content = {}

admin_Menu = MenuNode("Admin menu", content, main_menu=True)
admin_Menu.add_options(refillRequests_MenuNode)
MenuNode.default_node = admin_Menu
