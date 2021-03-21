from datetime import datetime
import time
from json_data_funcs import read_data_from_games_database, write_data_to_games_database
from json_data_funcs import read_data_from_users_database, write_data_to_users_database, json_serial


class User:
    n = 0
    logged = None

    def __init__(self, email=None, username=None, key=None, salt=None, dictionary=None, wallet=None):

        # Register and login details
        self.username = username
        self.key = key
        self.salt = salt
        self.email = email
        if not wallet:
            self.wallet = 0
        # self.games_history = {f'{g.name}': [] for g in Game.games_list}  # [users_top_score, datetime, game_id]
        self.id = User.n
        self.is_admin = False
        self.sent_request_box = []
        self.notifications = []
        if dictionary:
            for k in dictionary:
                setattr(self, k, dictionary[k])

    def __repr__(self):
        return self.username

    def clear_notifications(self):
        self.notifications = []

    def create_refill_request(self):
        all_users = read_data_from_users_database()
        administrators = all_users['admins']
        if len(administrators) > 0:
            while True:
                try:
                    amount = int(input("\nHow much do you need?\n"))
                    datetime_details = datetime.now()
                    datetime_details = json_serial(datetime_details)
                    approved = False
                    return {'user': self.username, 'amount': amount, 'datetime_details': datetime_details,
                            'approved': approved}
                except ValueError:
                    print("\nEnter a valid number.\n")
                    continue
        else:
            print("\nThere are currently no admins.\n")
            return

    @staticmethod
    def send_refill_request_to_admins(request):
        if request:
            # self.sent_request_box.append(request) TODO
            print("\nSending your request to administrators...\n")
            all_users = read_data_from_users_database()
            administrators = all_users['admins']
            for admin in administrators:
                admin['requests_box'].append(request)
                admin['notifications'].append(f"You have a new request from {request['user']}.")
            time.sleep(1)
            write_data_to_users_database(all_users)
            print("\nYour request is now being evaluated.\nIf not denied in 30 minutes, all requests are accepted "
                  "automatically.")
            return

    # def adding_user(self):
    #     User.n += 1


class GuestUser(User):
    m = 0
    default_wallet = 10

    def __init__(self):
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
        requests_box = admins[0]['requests_box']

    except KeyError:
        admins = []
        requests_box = []

    def __init__(self, email, username, key, salt, is_admin=True):

        # Both containers need to updated every time the admin class is run.

        self.requests_box = []  # List of dict objects.
        self.notifications = []

        all_users = read_data_from_users_database()
        admins = all_users['admins']
        for ad in admins:
            if ad['username'] == username:
                for req in ad['requests_box']:
                    self.requests_box.append(req)
                for notif in ad['notifications']:
                    self.notifications.append(notif)
        # TODO write to database
        super().__init__(email, username, key, salt, is_admin)
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

    def pending_requests_check(self):
        for req in self.requests_box:
            then = req["datetime_details"]
            now = datetime.now()
            seconds_diff = then.second - now.second
            if seconds_diff > 1800:
                req['approved'] = True

    def accept_all_requests(self):
        # TODO double check password verification
        for req in self.requests_box:
            req["approved"] = True

    def execute_requests(self):
        for req in self.requests_box:
            if req["approved"]:
                req["user"].wallet += req["amount"]
                req["user"].notifications.append(f"Your request for {req.amount} points has been accepted.")
