from structures.user_class import User


def logout():
    if User.user_logged:
        User.user_logged = None
