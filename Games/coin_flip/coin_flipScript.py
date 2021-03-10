import random
import time
import os
from datetime import datetime
from guestMenu.Register.json_users_funcs import read_data_from_users_database, write_data_to_users_database
from structures.user_class import User
from structures.game_class import Game
from structures.menu_Node import MenuNode


# Checking for player's history of this game


# game_id = 0


def start():
    coin_flip_game = Game('Coin Flip', User.user_logged)
    users_db_path = os.path.relpath("database/users.json")
    games_db_path = os.path.relpath('database/games.json')

    users = read_data_from_users_database()

    # Setting logged in user as playing user.
    playing_user = User.user_logged

    # Getting playing user's data from database.
    usr_dict = None
    for u in users['users']:
        if u['username'] == playing_user.username:
            usr_dict = u

    # Assigning database's data to playing user.
    playing_user = User(dictionary=usr_dict)

    # In the database we are looking for playing_user.games_history['CoinFlip']

    # users['users']

    # users_top_score = playing_user.games_history
    # if len(users_top_score) == 0:
    #     # means there are no games yet
    #     print("There are no games yet!")
    #     MenuNode.default_node()
    # coin_flip_top_5_scores = None

    register = 0
    choices = ["h", "t"]
    # game_id += 1
    score = 0
    current_game_results = []
    n = 2

    while True:
        if playing_user.wallet == 0:
            for sec in range(n):
                print("You have no money in your wallet. Please refill your wallet or sit and just watch the menu.")
                time.sleep(n)
                MenuNode.current_node()

        # Choosing randomly ("H", "T").
        drawn_value = random.choice(choices)

        # Getting player's bet.
        try:
            players_money_bet = int(input
                                    (f"\nYou currently have {playing_user.wallet} "
                                     f"in your wallet. How much do you want to bet? Enter a positive number:\n\n"))
            if players_money_bet <= 0:
                print("\nYou must enter a positive number.")
                time.sleep(2)
                continue
            if players_money_bet > playing_user.wallet:
                print("\nYou don't have that much money in your wallet!")
                time.sleep(2)
                continue
            playing_user.wallet -= players_money_bet
            register += players_money_bet

        except ValueError:
            print("Please enter valid number.")
            continue

        # Getting player's choice input
        players_choice = input("""
    
        What is your bet? 
    
        Heads or tails?
    
        Enter H or T.
    
        """)

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
                    ['W', f"Money bet: {players_money_bet}", f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])
                score += players_money_bet
                register -= 2 * players_money_bet
                # winning animation
            else:
                print("You lost! :( ")
                score -= players_money_bet
                current_game_results.append(
                    ['L', f"Money bet: {players_money_bet}", f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])
                time.sleep(1)

                # money countdown animation
            print(f"\nCurrent's session score: {2*score}.")
            print(f"\nCurrent's session won points: {score}.")
            print(f"\nCurrent's session results: {current_game_results}.")
            print(f"\nYour wallet's status: {playing_user.wallet}.")

            next_input = input("\n\nDo you want to play again? Enter E to exit or any other character to play "
                               "again.\n\n")
            if not next_input.lower() == "e":
                continue
            else:
                playing_user.wallet += score
                if score >= 0:
                    print(f'\nYou won {abs(score)}'
                          f' points in this session.\nCurrently in your wallet:\n{playing_user.wallet}')
                    break
                else:
                    print(f'\nYou lost {abs(score)} '
                          f'points in this session.\nCurrently in your wallet:\n{playing_user.wallet}')
                    break

    playing_user_dict = playing_user.__dict__
    for u in users['users']:
        if u['username'] == playing_user_dict['username']:
            users['users'].append(playing_user_dict)
            del u

    write_data_to_users_database(users)
    print(f'Returning to {MenuNode.default_node.name}.')
    time.sleep(1)
    MenuNode.default_node()



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
