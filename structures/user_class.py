from json_data_funcs import read_data_from_games_database
from json_data_funcs import read_data_from_users_database, write_data_to_users_database
from json_data_funcs import read_data_from_admins_database, write_data_to_admins_database


class User:
    # admins = read_data_from_admins_database()
    logged = None
    # user_id = admins['admins_inf']['user_id']

    def __init__(self, email=None, username=None, key=None, salt=None, dictionary=None, wallet=None, is_admin=False):
        users = read_data_from_users_database()
        admins = read_data_from_admins_database()

        if dictionary is None:
            self.user_id = admins['admins_inf']['user_id']
            admins['admins_inf']['user_id'] += 1
            write_data_to_admins_database(admins)

        self.notifications = []

        for us in users['users']:
            if us['username'] == username:
                self.notifications = us['notifications']

        # Register and login details
        self.username = username
        self.key = key
        self.salt = salt
        self.email = email
        if not wallet:
            self.wallet = 0
        # self.games_history = {f'{g.name}': [] for g in Game.games_list}  # [users_top_score, datetime, game_id]
        self.is_admin = is_admin
        self.sent_request_box = []

        if dictionary:
            self.dictionary = dictionary
            for k in self.dictionary.keys():
                setattr(self, k, self.dictionary[k])

    def __repr__(self):
        return self.username

    def clear_notifications(self):
        self.notifications = []


class GuestUser(User):
    def __init__(self):
        admins = read_data_from_admins_database()
        users = read_data_from_users_database()
        try:
            self.guest_id = admins['admins_inf']['guest_id']
        except KeyError:
            users['admins_inf']['guest_id'] = 0
            self.guest_id = admins['admins_inf']['guest_id']

        try:
            self.default_wallet = admins['admins_inf']['guest_wallet']
        except KeyError:
            users['users_inf']['wallet'] = 10
            self.guest_id = admins['admins_inf']['guest_wallet']

        super().__init__()
        admins['admins_inf']['guest_id'] += 1
        self.username = f"Guest{self.guest_id}"
        self.wallet = self.default_wallet
        write_data_to_users_database(users)


class Admin(User):

    def __init__(self, email, username, key, salt, is_admin=True, dictionary=None):
        admins = read_data_from_admins_database()
        super().__init__(email, username, key, salt, dictionary)
        self.is_admin = is_admin
        self.notifications = []

        for ad in admins['admins']:
            if ad['username'] == username:
                for notif in ad['notifications']:
                    self.notifications.append(notif)

    def __repr__(self):
        return self.username

