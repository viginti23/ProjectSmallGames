import random
import time
import os
from datetime import datetime
from guestMenu.Register.json_users_funcs import read_data_from_users_database, write_data_to_users_database
from structures.user_class import User, GuestUser
from structures.game_class import Game
from structures.menu_Node import MenuNode


class CoinF(Game):
    game_id = 0
    game_register = 0

    def __init__(self, name, user):
        self.game_id = CoinF.game_id
        CoinF.game_id += 1
        super().__init__(name, user)

    def __call__(self, *args, **kwargs):
        return self.start_game()

    def start_game(self):
        # users_db_path = os.path.relpath("database/users.json")
        # games_db_path = os.path.relpath('database/games.json')

        choices = ["h", "t"]
        score = 0
        current_game_results = []
        n = 5
        if User.user_logged:
            playing_user = self.settingUser()
        else:
            playing_user = self.settingGuestUser()

        while True:
            if playing_user.wallet == 0:
                for sec in range(n):
                    print("You have no money in your wallet. Please refill your wallet or sit and just watch the menu.")
                    time.sleep(n)
                    MenuNode.current_node()

            # Choosing randomly ("H", "T").
            drawn_value = random.choice(choices)

            # Getting player's money bet
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
                    print("HEADS!")
                elif drawn_value.lower() == "t":
                    print("TAILS!")
                time.sleep(1)

            if players_choice.lower() == drawn_value.lower():
                print("You won!!!")
                time.sleep(1)
                current_game_results.append(
                    ['W', f"Money bet: {players_money_bet}",
                     f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])
                playing_user.wallet += players_money_bet
                if isinstance(playing_user, User):
                    CoinF.game_register -= players_money_bet
                score += players_money_bet
                # winning animation

            else:
                print("You lost! :( ")
                time.sleep(1)
                playing_user.wallet -= players_money_bet
                if isinstance(playing_user, User):
                    CoinF.game_register += players_money_bet
                score -= players_money_bet
                current_game_results.append(
                    ['L', f"Money bet: {players_money_bet}",
                     f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])
                # money countdown animation

            print(f"\nSession's score: {score}.")
            print(f"\nCurrent's session results: {current_game_results}.")
            print(f"\nYour wallet's status: {playing_user.wallet}.")

            next_input = input("\n\nDo you want to play again? Enter E to exit or any other character to play "
                               "again.\n\n")
            if not next_input.lower() == "e":
                continue
            else:
                if score >= 0:
                    print(f'\nYou won {abs(score)}'
                          f' points in this session.\nCurrently in your wallet:\n{playing_user.wallet}')
                    break
                else:
                    print(f'\nYou lost {abs(score)} '
                          f'points in this session.\nCurrently in your wallet:\n{playing_user.wallet}')
                    break
        if isinstance(playing_user, User):
            self.saving_users_score(playing_user)

    # In the database we are looking for playing_user.games_history['CoinFlip']
    # users['users']

    # users_top_score = playing_user.games_history
    # if len(users_top_score) == 0:
    #     # means there are no games yet
    #     print("There are no games yet!")
    #     MenuNode.default_node()
    # coin_flip_top_5_scores = None

    # # Checking if User has played this game and storing up to 10 games in memory.
    # if User.user_logged:
    #     if User.user_logged.games_history.get("FlippingCoin") is None:
    #         User.user_logged.games_history["FlippingCoin"] = []
    #     else:
    #         if len(user.games_history["FlippingCoin"]) < 10:
    #             user.games_history["FlippingCoin"].append(result)
    #         else:
    #             del user.games_history["FlippingCoin"][0]
    #             user.games_history["FlippingCoin"].append(result)
    #
