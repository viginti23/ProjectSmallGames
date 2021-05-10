import time
from datetime import datetime
import os
from structures.user_class import User, GuestUser
from structures.menu_Node import MenuNode
from json_data_funcs import read_data_from_games_database, write_data_to_games_database, read_data_from_users_database,\
    write_data_to_users_database


# Parent class for each game.
class Game:
    games = read_data_from_games_database()
    current_game = ""
    # Total system's register status.
    try:
        total_register = games['games_inf']['total_register']
    except KeyError:
        games['games_inf']['total_register'] = 0
        total_register = games['games_inf']['total_register']

    def __init__(self, name):
        self.name = name
        games = read_data_from_games_database()
        if self.name not in games['games'].keys():
            games['games'][self.name] = self.__dict__
            games['games'][self.name]['game_id'] = games['games_inf']['game_id']
            games['games_inf']['game_id'] += 1

        try:
            self.register = games['games'][self.name]['register']
        except KeyError:
            games['games'][self.name]['register'] = 0
            self.register = games['games'][self.name]['register']

        try:
            self.top5 = games['games'][self.name]['top5']
        except KeyError:
            games['games'][self.name]['top5'] = []
            self.top5 = games['games'][self.name]['top5']

        write_data_to_games_database(games)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @staticmethod
    def get_result_obj(score, playing_user):
        return {'username': playing_user.username,
                'score': score,
                'datetime_details': datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M')}

    def check_top_n(self, score, n=5):
        games = read_data_from_games_database()
        try:
            top5: list = games['games'][self.name]['top5']
        except KeyError:
            games['games'][self.name]['top5'] = []
            top5 = games['games'][self.name]['top5']
        from structures.user_class import User
        playing_user = User.logged
        new_top_result = self.get_result_obj(score, playing_user)
        top5.append(new_top_result)
        top5.sort(key=lambda x: x['score'], reverse=True)
        try:
            top5 = top5[:n]
        except IndexError:
            top5 = top5
        if top5[-1]['score'] <= score:
            print('\n\nYour score has reached TOP 5!\n\n')
            time.sleep(2)
        write_data_to_games_database(games)

    @staticmethod
    def display_top_n(gamename, n=5):
        os.system('clear')
        games = read_data_from_games_database()
        try:
            top5 = games['games'][gamename]['top5']
        except KeyError:
            games['games'][gamename] = {}
            games['games'][gamename]['top5'] = []
            top5 = games['games'][gamename]['top5']

        if len(top5) == 0:
            print('\nThere are no records yet!\n')
        else:
            top5.sort(key=lambda x: x['score'], reverse=True)
            top5 = top5[:n]
            print('\n\n\n')
            for i, result in enumerate(top5):
                print(f"{i + 1}| {result['username']} | {result['score']} | {result['datetime_details']}\n")

        inp = input('\nPress Enter to continue.\n')
        return MenuNode.current_node()

    @staticmethod
    def display_personal_best(gamename):
        users = read_data_from_users_database()
        playing_user = User.logged
        for user in users['users']:
            if user['username'] == playing_user.username:
                try:
                    game_best = user['my_best'][gamename]
                except KeyError:
                    user['my_best'][gamename] = {}
                    user['my_best'][gamename]['score'] = 0
                    game_best = user['my_best'][gamename]
                write_data_to_users_database(users)
                print(f"\nYour personal best in {gamename} is:\n"
                      f"\t\t\t{game_best['score']} points.\n")
        inp = input("\nPress Enter to continue.\n")
        return MenuNode.current_node()

    def check_personal_best(self, score):
        users = read_data_from_users_database()

        from structures.user_class import User
        playing_user = User.logged

        curr_result = self.get_result_obj(score, playing_user)

        for user in users['users']:
            if user['username'] == curr_result['username']:

                try:
                    game_best = user['my_best'][self.name]
                    if curr_result['score'] > game_best['score']:
                        user['my_best'][self.name] = curr_result
                        print("\n\n\nNEW PERSONAL BEST!\n\n\n")

                except KeyError:
                    user['my_best'][self.name] = curr_result
                    game_best = user['my_best'][self.name]

        write_data_to_users_database(users)

    def round_end(self, score, playing_user):
        # Returns True if we want to exit.
        next_input = input("\n\nDo you want to play again? Enter E to exit or any other character to play "
                           "again.\n\n")

        if next_input.lower() == "e":

            if score >= 0:
                print(f'\nYou won {abs(score)}'
                      f' points in this session.\nCurrently in your wallet:\n{playing_user.wallet}')

            else:
                print(f'\nYou lost {abs(score)} '
                      f'points in this session.\nCurrently in your wallet:\n{playing_user.wallet}')
            # Checking if the score is high enough to get to top 5 results of the game or to the personal best.
            if not isinstance(playing_user, GuestUser):
                self.check_top_n(score)
                self.check_personal_best(score)
            return True
        else:
            return False

    @staticmethod
    def system_wallet():
        games = read_data_from_games_database()
        total_register = games['games_inf']['total_register']

        for gamename in games['games']:
            print(f"\n{gamename}: {games['games'][gamename]['register']}\n")
            total_register += games['games'][gamename]['register']
        write_data_to_games_database(games)
        from structures.user_class import User
        if User.logged.is_admin:
            print(f"Total number of points in the system:\n{total_register}\n")
            inp = input("Press Enter to continue.")
            return MenuNode.current_node()
            # print each game separately

    @staticmethod
    def setting_player():
        from structures.user_class import User
        if User.logged:
            return User.logged
        else:
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

    @staticmethod
    def not_enough_money(wallet):
        if wallet <= 0:
            print("You have no money in your wallet. Please refill your wallet or sit and just watch the menu.")
            time.sleep(3)
            return MenuNode.current_node()

    @staticmethod
    def start_game(game):

        playing_user = game.setting_player()
        while True:

            players_choice, drawn_value, players_money_bet = game.game(playing_user)
            game.evaluating_results(players_choice, drawn_value, players_money_bet, playing_user)

            print(f"\nSession's score: {game.score}.")
            print(f"\nCurrent's session results: {game.current_session_results}.")
            print(f"\nYour wallet's status: {playing_user.wallet}.")

            # Updating user's wallet in the database
            if User.logged:
                users = read_data_from_users_database()
                for user in users['users']:
                    if user['username'] == playing_user.username:
                        user['wallet'] += game.score
                write_data_to_users_database(users)

            # Updating game's register in the database.
            games = read_data_from_games_database()
            games['games'][game.name]['register'] += -game.score
            write_data_to_games_database(games)

            rnd = game.round_end(game.score, playing_user)
            if rnd:
                break
            else:
                continue
        print("Coming back to the previous menu...")
        time.sleep(5)
        return MenuNode.current_node()
