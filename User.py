class GuestUser:
    n = 0

    def __init__(self, n, wallet=0):
        n += 1
        self.username = f"Guest{n}"
        self.logged_in = False
        self.wallet = wallet


class User:
    n = 0
    user_logged = None

    def __init__(self, email, username, password, wallet=0):
        self.username = username
        self.password = password
        self.email = email
        self.my_wallet = wallet
        self.user_id = User.n
        User.n += 1
        self.records = {}
