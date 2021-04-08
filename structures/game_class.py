import time
from structures.user_class import User, GuestUser
from json_data_funcs import read_data_from_games_database, write_data_to_games_database


# Parent class for each game.
class Game:

    games_list = []  # TODO adding new games functionality

    # Total system's register status.
    total_register = 0
    for game in games_list:
        total_register += game.game_register  # TODO save to database
    game_id = len(games_list)

    def __init__(self, name, user):
        self.name = name
        self.user = user
        Game.games_list.append(self)  # TODO check if it appends all instances or just when we add new games

    def __repr__(self):
        return self.name

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
