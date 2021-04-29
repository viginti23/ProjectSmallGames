import time
from structures.user_class import User, GuestUser
from json_data_funcs import read_data_from_games_database, write_data_to_games_database, read_data_from_admins_database, write_data_to_admins_database


# Parent class for each game.
class Game:
    games = read_data_from_games_database()
    # Total system's register status.
    try:
        total_register = games['games_inf']['total_register']
    except KeyError:
        games['games_inf']['total_register'] = 0
        total_register = games['games_inf']['total_register']

    try:
        game_id = games['games_inf']['game_id']
    except KeyError:
        games['games_inf']['game_id'] = 0
        game_id = games['games_inf']['game_id']
    write_data_to_games_database(games)

    def __init__(self, name):
        self.name = name
        games = read_data_from_games_database()

        if self not in games['games']:
            games['games'][self.name] = self.__dict__
            write_data_to_games_database(games)
        self.game_id = games['games_inf']['game_id'] + 1
        games['games_inf']['game_id'] += 1
        write_data_to_games_database(games)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


    @staticmethod
    def system_wallet():
        if User.logged.is_admin:
            return Game.total_register
            # print each game separately

    @staticmethod
    def settingUser():
        # Setting the logged in user as playing user.
        return User.logged

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

    def get_top5(self):
        top5 = None
        if User.logged:
            top5 = []
            games = read_data_from_games_database()
            if games['games']:
                for g in games['games']:
                    if g['name'] == f'{self.name}':
                        top5 = g['top5']
            else:
                top5 = []
        return top5
