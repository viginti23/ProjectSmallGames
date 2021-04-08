from json_data_funcs import read_data_from_games_database
from json_data_funcs import read_data_from_users_database, write_data_to_users_database


class User:
    all_users = read_data_from_users_database()
    n = len(all_users['users']) + 1
    logged = None

    def __init__(self, email=None, username=None, key=None, salt=None, dictionary=None, wallet=None, is_admin=False,
                 user_id=n):

        # Register and login details
        self.username = username
        self.key = key
        self.salt = salt
        self.email = email
        if not wallet:
            self.wallet = 0
        # self.games_history = {f'{g.name}': [] for g in Game.games_list}  # [users_top_score, datetime, game_id]
        self.user_id = user_id
        self.is_admin = is_admin
        self.sent_request_box = []
        self.notifications = []
        if dictionary:
            self.dictionary = dictionary
            for k in self.dictionary.keys():
                setattr(self, k, self.dictionary[k])

    def __repr__(self):
        return self.username

    def clear_notifications(self):
        self.notifications = []


class GuestUser(User):
    m = 0
    default_wallet = 10

    def __init__(self):
        # read_data_from_users_database()
        super().__init__()
        GuestUser.m += 1
        self.username = f"Guest{GuestUser.m}"
        self.wallet = GuestUser.default_wallet
    # TODO database2


class Admin(User):
    all_users = read_data_from_users_database()
    admins = None
    requests_box = None

    try:
        admins = all_users['admins']
        requests_box = admins[-1]['requests_box']
    except IndexError:
        admins = []
        requests_box = []
    except KeyError:
        admins = []
        requests_box = []

    def __init__(self, email, username, key, salt, is_admin=True, dictionary=None):
        all_users = read_data_from_users_database()
        super().__init__(email, username, key, salt, dictionary)
        self.is_admin = is_admin
        self.notifications = []
        self.requests_box = []

        admins = all_users['admins']
        for ad in admins:
            if ad['username'] == username:
                for notif in ad['notifications']:
                    self.notifications.append(notif)
            if Admin.requests_box:
                self.requests_box = Admin.requests_box  # probably unnecessary line
        write_data_to_users_database(admins)

    def __repr__(self):
        return self.username

    def system_wallet(self):
        if self.logged.is_admin:
            games = read_data_from_games_database()
            total = 0
            try:
                for game in games:
                    total += game['register']
            except KeyError:
                print("There are no games yet.")
            return total

    def req_1_by_1(self):
        for req in self.requests_box:
            print(req)

    def accept_all_requests(self):
        # TODO double check password verification
        for req in self.requests_box:
            req["approved"] = True
