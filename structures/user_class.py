import json
from datetime import datetime
import time
from json import JSONEncoder
from types import SimpleNamespace as Namespace
# from structures.game_class import Game


class GuestUser:
    m = 0
    default_wallet = 10

    def __init__(self, n=m):
        n += 1
        self.username = f"Guest{n}"
        self.wallet = GuestUser.default_wallet


class User:
    n = 0
    user_logged = None

    def __init__(self, email=None, username=None, key=None, salt=None, dictionary=None, wallet=None, is_admin=False):

        # Register and login details
        self.username = username
        self.key = key
        self.salt = salt
        self.email = email
        if not wallet:
            self.wallet = 0
        # self.games_history = {f'{g.name}': [] for g in Game.games_list}  # [users_top_score, datetime, game_id]
        self.id = User.n
        self.is_admin = is_admin
        self.sent_request_box = []
        self.notifications = []
        if dictionary:
            for k in dictionary:
                setattr(self, k, dictionary[k])

    def __repr__(self):
        return self.username

    def clear_notifications(self):
        self.notifications = []

    def get_refill_request(self):
        if len(Admin.admins) > 0:
            while True:
                try:
                    amount = int(input("\nHow much do you need?\n"))
                    datetime_details = datetime.now()
                    approved = False
                    request = {'user': self, 'amount': amount, 'datetime_details': datetime_details,
                               'approved': approved}
                    return request
                except ValueError:
                    print("Enter a valid number.")
                    continue

    def send_refill_request_to_admins(self, request):
        print("\nSending your request to administrators...\n")
        self.sent_request_box.append(request[self])
        for admin in Admin.admins:
            admin.requests_box.append(request)
            admin.notifications.append(f"You have a new request from {self.username}.")
        time.sleep(1)
        print("\nYour request is now being evaluated.\nIf not denied in 30 minutes, all requests are accepted "
              "automatically.")


    # def adding_user(self):
    #     User.n += 1


class Admin(User):
    admins = []

    def __init__(self, email, username, key, salt, dictionary, wallet, is_admin=True):
        self.requests_box = []  # list of dicts
        super().__init__(email, username, key, salt, dictionary, wallet, is_admin)
        if len(Admin.admins) < 2:
            Admin.admins.append(self)

    # suma wszystkich wygranych gier przez komputer (bank systemu)
    def requests_queue(self):
        for req in self.requests_box:
            print(req + '\n')

    def pending_requests_check(self):
        for req in self.requests_box:
            then = req["datetime_details"]
            now = datetime.now()
            seconds_diff = then.second - now.second
            if seconds_diff > 1800:
                req['approved'] = True

    def accept_all_requests(self):
        # TODO password verification
        for req in self.requests_box:
            req["approved"] = True

    def execute_requests(self):
        for req in self.requests_box:
            if req["approved"]:
                req["user"].wallet += req["amount"]
                req["user"].notifications.append(f"Your request for {req.amount} points has been accepted.")
