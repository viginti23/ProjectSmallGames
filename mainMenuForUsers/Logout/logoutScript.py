from structures.user_class import User, Admin


def logout():
    if Admin.logged:
        Admin.logged = None

    if User.logged:
        User.logged = None
