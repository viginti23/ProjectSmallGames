import time
from json_data_funcs import read_data_from_users_database, write_data_to_users_database
from structures.user_class import User, GuestUser
from json_data_funcs import read_data_from_games_database, write_data_to_games_database


# Parent class for each game.
class Game:
    games_list = []  # TODO adding new games functionality

    # Total system's register status.
    total_register = 0
    for game in games_list:
        total_register += game.game_register

    game_id = len(games_list)

    def __init__(self, name, user):
        self.name = name
        self.user = user
        Game.games_list.append(self) # TODO check if it appends all instances or just when we add new games

    def __repr__(self):
        return self.name

    def show_best_scores(self):
        games = read_data_from_games_database()
        for game in games['games']:
            if game['name'] == self.name:
                return game['top5']

    @staticmethod
    def settingUser():
        users = read_data_from_users_database()

        # Setting the logged in user as playing user.
        player = User.user_logged

        # Getting playing user's data from database.
        usr_dict = None
        for u in users['users']:
            if u['username'] == player.username:
                usr_dict = u

        # Assigning database's data to playing user class object.
        return User(dictionary=usr_dict)

    @staticmethod
    def saving_users_score(usr):
        users = read_data_from_users_database()
        playing_user_dict = usr.__dict__
        for u in users['users']:
            if u['username'] == playing_user_dict['username']:
                users['users'].append(playing_user_dict)
                del u
        write_data_to_users_database(users)

    @staticmethod
    def settingGuestUser():
        return GuestUser()

    @staticmethod
    def getting_players_bet(player):
        # Getting player's bet.
        while True:
            try:
                players_money_bet = int(input
                                        (f"\nYou currently have {player.wallet} "
                                         f"in your wallet. How much do you want to bet? Enter a positive number:\n\n"))

                if players_money_bet <= 0:
                    print("\nYou must enter a positive number.")
                    time.sleep(2)
                    continue
                if isinstance(player, User):
                    if players_money_bet > player.wallet:
                        print("\nYou don't have that much money in your wallet!")
                        time.sleep(2)
                        continue
                return players_money_bet

            except ValueError:
                print("Please enter valid number.")
                continue
