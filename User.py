import _sha256


class GuestUser:
    n = 0

    def __init__(self, n):
        n += 1
        self.username = f"Guest{n}"
        self.logged_in = False


class User:
    def __init__(self, username, password, wallet):
        self.username = username
        self.password = password
        self.my_wallet = wallet
