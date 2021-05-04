import random
import time
from datetime import datetime
from structures.user_class import User
from structures.game_class import Game
from structures.menu_Node import MenuNode
import json_data_funcs


class CoinF(Game):
    def __init__(self):
        super().__init__(name='Coin Flip')

    def __call__(self):
        return self.start_game()

    def start_game(self):

        choices = ["h", "t"]
        score = 0
        current_session_results = []
        if User.logged:
            playing_user = self.settingUser()
        else:
            playing_user = self.settingGuestUser()

        while True:
            if playing_user.wallet == 0:
                print("You have no money in your wallet. Please refill your wallet or sit and just watch the menu.")
                time.sleep(3)
                return MenuNode.current_node()

            # Choosing randomly ("H", "T").
            drawn_value = random.choice(choices)

            # Getting player's points bet
            players_money_bet = self.getting_players_bet(playing_user)

            # Getting player's choice input
            players_choice = input("""
        
            What is your bet? 
        
            Heads or tails?
        
            Enter H or T.
        
            """)

            # Evaluating results.
            if players_choice.lower() not in choices:
                print("Enter H or T.")
                continue
            else:
                print("Throwing the coin!")
                time.sleep(0.5)
                print("\n...\n")
                time.sleep(0.5)
                print("\n..\n")
                time.sleep(0.5)
                print("\n.\n")
                if drawn_value.lower() == "h":
                    print("HEADS!\n")
                elif drawn_value.lower() == "t":
                    print("TAILS!\n")
                time.sleep(1)

            wins_strike = 0
            loses_strike = 0

            if players_choice.lower() == drawn_value.lower():
                print("You won!!!")
                loses_strike = 0
                wins_strike += 1
                time.sleep(1)
                current_session_results.append(
                    ['W', f"Money bet: {players_money_bet}",
                     f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])
                # Money the user bet coming back to the wallet:
                playing_user.wallet += players_money_bet

                # Transferring the won money to the user ('score' is a temporary session's wallet only for gained money).
                # if isinstance(playing_user, User):
                self.register -= players_money_bet
                score += players_money_bet


                # winning animation
            else:
                print("You lost! :( ")
                loses_strike += 1
                wins_strike = 0
                time.sleep(1)
                playing_user.wallet -= players_money_bet
                self.register += players_money_bet
                games = json_data_funcs.read_data_from_games_database()
                games['games'][self.name]['register'] += players_money_bet

                score -= players_money_bet
                current_session_results.append(
                    ['L', f"Money bet: {players_money_bet}",
                     f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])
                # money countdown animation

            games = json_data_funcs.read_data_from_games_database()
            games['games'][self.name]['register'] = self.register

            print(f"\nSession's score: {score}.")
            print(f"\nCurrent's session results: {current_session_results}.")
            print(f"\nYour wallet's status: {playing_user.wallet}.")

            users = json_data_funcs.read_data_from_users_database()
            for user in users['users']:
                if user['username'] == playing_user.username:
                    user['wallet'] += score
            json_data_funcs.write_data_to_users_database(users)

            rnd = self.round_end(score, playing_user)
            if rnd:
                break
            else:
                continue

        print("Coming back to the previous menu...")
        time.sleep(5)
        return MenuNode.current_node()
