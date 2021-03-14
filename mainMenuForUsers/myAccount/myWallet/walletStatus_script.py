from structures.user_class import User


def wallet_status():
    user = User.user_logged
    return user.wallet
