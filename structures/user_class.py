from datetime import datetime
import time
from json_data_funcs import read_data_from_users_database
from guestMenu.main_Menu import MainMenu
from mainMenuForUsers.mainMenu_forUsers import MainMenuForUsers
from adminMenu.admin_menu import admin_Menu




class User:
    n = 0
    user_logged = None
    if user_logged is None:
        default_node = MainMenu

    def __init__(self, email=None, username=None, key=None, salt=None, dictionary=None, wallet=None,
                 is_admin=False):

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

    def create_refill_request(self):
        if len(Admin.admins) > 0:
            while True:
                try:
                    amount = int(input("\nHow much do you need?\n"))
                    datetime_details = datetime.now()
                    approved = False
                    return {'user': self, 'amount': amount, 'datetime_details': datetime_details,
                            'approved': approved}
                except ValueError:
                    print("Enter a valid number.")
                    continue
        else:
            print("There are currently no admins.")
            return

    def send_refill_request_to_admins(self, request):
        print("\nSending your request to administrators...\n")
        self.sent_request_box.append(request)
        for admin in Admin.admins:
            admin['requests_box'].append(request)
            admin['notifications'].append(f"You have a new request from {self.username}.")
        time.sleep(1)
        print("\nYour request is now being evaluated.\nIf not denied in 30 minutes, all requests are accepted "
              "automatically.")
        return

    # def adding_user(self):
    #     User.n += 1


class GuestUser(User):
    m = 0
    default_wallet = 10
    default_node = MainMenu

    def __init__(self):
        super().__init__()
        GuestUser.m += 1
        self.username = f"Guest{n}"
        self.wallet = GuestUser.default_wallet
    # TODO database


class Admin(User):
    all_users = read_data_from_users_database()
    admins = None

    default_node = admin_Menu

    try:
        admins = all_users['admins']
    except KeyError:
        admins = []

    def __init__(self, email, username, key, salt):
        self.requests_box = []  # list of dict objects
        super().__init__(email, username, key, salt, is_admin=True)

    def __repr__(self):
        return self.username

    # suma wszystkich wygranych gier przez komputer (bank system access)
    def requests_queue(self):
        for req in self.requests_box:
            print(f"------> {req['username']}\t{req.amount}\n")

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
