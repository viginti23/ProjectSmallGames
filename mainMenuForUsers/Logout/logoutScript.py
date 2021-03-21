from structures.user_class import User


def logout():
    if User.logged:
        User.logged = None
