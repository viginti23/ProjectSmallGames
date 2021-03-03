import json
from json import JSONEncoder
from types import SimpleNamespace as Namespace


class GuestUser:
    n = 0

    def __init__(self, n, wallet=0):
        n += 1
        self.username = f"Guest{n}"
        self.wallet = wallet


class User:
    n = 0
    user_logged = None

    def __init__(self, email=None, username=None, key=None, salt=None, dictionary=None, wallet=0):
        self.username = username
        self.id = User.n
        User.n += 1
        self.key = key
        self.salt = salt
        self.email = email
        self.wallet = wallet
        self.records = {}
        self.history = {f'{}' for k,v in 'game/Game.gameslist'}
        if dictionary:
            for k in dictionary:
                setattr(self, k, dictionary[k])

    def __repr__(self):
        return self.username


