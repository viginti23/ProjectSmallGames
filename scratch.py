# import json
# from User import User
# # from MainMenu import MainMenu
# # valid_email = 'zarodm@wp.pl'
# # valid_username = 'viginti'
# # valid_hashed_password = 'asd'
# #
# # new_user = User(valid_email, valid_username, valid_hashed_password)
# # print(new_user.__dict__)
# # print("You can now log in.")
#
#
# def printing_menu_view(menu_node):
#     for option in menu_node.content.keys():
#         print(menu_node.content.get(option))
#
#
# print(callable(printing_menu_view))

from MenuNode import MenuNode


content = {'1': '1 Start',
           '2': '2 Results'}

ccc = MenuNode("ccc", content)

print(ccc.__dict__)