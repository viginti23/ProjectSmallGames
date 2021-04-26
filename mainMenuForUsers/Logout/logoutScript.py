from structures.menu_Node import MenuNode


def logout():
    from structures.user_class import User, Admin

    if User.logged:
        if User.logged.is_admin:
            Admin.logged = None
        User.logged = None

    from guestMenu.main_Menu import MainMenu
    MenuNode.default_node = MainMenu
    MenuNode.current_node = MainMenu
    return MenuNode.default_node()
