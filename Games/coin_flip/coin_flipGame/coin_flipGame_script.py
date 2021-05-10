import os
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
        self.score = 0
        self.current_session_results = []

    # def __call__(self):
    #     return self.start_game()

    def evaluating_results(self, players_choice, drawn_value, players_money_bet, playing_user):

        # Evaluating results.
        if players_choice.lower() == drawn_value.lower():
            print("You won!!!")

            time.sleep(1)

            self.current_session_results.append(
                ['W', f"Money bet: {players_money_bet}",
                 f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])

            # Money the user bet coming back to the wallet:
            playing_user.wallet += players_money_bet

            # Transferring the won money to the user ('score' is a temporary session's wallet only for gained
            # money).
            self.register -= players_money_bet
            self.score += players_money_bet

            # winning animation
        else:
            print("You lost! :( ")
            time.sleep(1)
            self.current_session_results.append(
                ['L', f"Money bet: {players_money_bet}",
                 f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])

            playing_user.wallet -= players_money_bet
            self.register += players_money_bet

            self.score -= players_money_bet

    def game(self, playing_user):
        while True:

            self.not_enough_money(playing_user.wallet)

            choices = ["h", "t"]

            # Getting player's points bet
            players_money_bet = self.getting_players_bet(playing_user)
            chosen_bet = ''
            while True:
                # Getting player's choice input
                os.system('clear')
                players_choice = input("""
            
                                Heads or tails?
            
                                Enter H or T.
            
                                """)

                if players_choice.lower() not in choices:
                    print("Enter H or T.")
                    continue
                else:
                    break

            print("Throwing the coin!")
            time.sleep(0.5)
            print("\n...\n")
            time.sleep(0.5)
            print("\n..\n")
            time.sleep(0.5)
            print("\n.\n")

            # Choosing randomly ("H", "T").
            drawn_value = random.choice(choices)

            if drawn_value.lower() == "h":
                print("\nHEADS!\n")
            elif drawn_value.lower() == "t":
                print("\nTAILS!\n")
            time.sleep(1)
            return players_choice, drawn_value, players_money_bet
