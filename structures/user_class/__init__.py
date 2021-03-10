import json
from json import JSONEncoder
from types import SimpleNamespace as Namespace
from structures.game_class import Game


class GuestUser:
    n = 0

    def __init__(self, n, wallet=0):
        n += 1
        self.username = f"Guest{n}"
        self.wallet = wallet

# OPRÓĆZ IMPORTU Z JAKIEGOS PLIKU RÓB: USer.n += 1, Z WYJĄTKIEM TEGO PLIKU, GDZIE TEGO NIE ROBIMY


class User:
    n = 0
    user_logged = None

    def __init__(self, email=None, username=None, key=None, salt=None, dictionary=None, wallet=None):

        # Register and login details
        self.username = username
        self.key = key
        self.salt = salt
        self.email = email
        if not wallet:
            self.wallet = 0
        self.games_history = {f'{g.name}': [] for g in Game.games_list}   # [users_top_score, datetime, game_id]
        self.id = User.n

        if dictionary:
            for k in dictionary:
                setattr(self, k, dictionary[k])

    def __repr__(self):
        return self.username

    # def adding_user(self):
    #     User.n += 1

