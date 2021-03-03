import random
import time
from User import User


class CoinFlip()
    game_name = "Flipping Coin"
    game_played = 0
    values = ["H", "T"]
    wallet = 0  # how much money the game can win
    playing_user = str(User.user_logged)

    # games1.add_game(self)

    def __init__(self, user):  # settingsy gry, plus default settings
        # przy tworzeniu instancji gry, gra sprawdza czy user jest zalogowany
        # jeśli jest, to przejmuje historię usera, jego wallet, etc
        # jeśli nie, to tworzy tymczasowego usera i tymczasowy wallet
        # if not user.logged_in:
        #     guest_name = f"Guest{CoinFlip.game_played + 1}"
        #     self.user = GuestUser(guest_name)  # default value of wallet is 10
        #     print(f"You are staring with {user.users_wallet} USD.")
        # else:  # if user is logged in
        #     self.user = user
        #     print(f"You have {user.users_wallet} USD in your wallet.")
        pass

    def __call__(self):
        return self.start_game()

    def __repr__(self):
        return CoinFlip.game_name

    def start_game(self):
        result = None
        while True:


            # Checking if User has played this game and storing up to 10 games in memory.
            if User.user_logged:
                if User.user_logged.games_history.get("FlippingCoin") is None:
                    User.user_logged.games_history["FlippingCoin"] = []
                else:
                    if len(user.games_history["FlippingCoin"]) < 10:
                        user.games_history["FlippingCoin"].append(result)
                    else:
                        del user.games_history["FlippingCoin"][0]
                        user.games_history["FlippingCoin"].append(result)


            # Choosing randomly ("H", "T")
            chosen_value = random.choice(["H","T"])  # Here, we have now either "Heads" or "Tails"


            while True:
                players_money_bet = int(input("How much do you want to bet? Enter a positive number:\n\n"))
                if players_money_bet <= 0:
                    print("You must enter a positive number.")
                    time.sleep(2)
                    continue
                elif players_money_bet > user.users_wallet:
                    print("You don't have that much money in your wallet!")
                    time.sleep(2)
                    continue
                else:
                    break
            user.users_wallet -= players_money_bet
            self.wallet += players_money_bet

            try:
                players_bet = input("""

                What is your bet? 

                Heads or tails?

                Enter H or T.

                """)

                print("Throwing the coin!")
                time.sleep(2)
                if chosen_value.lower() == "h":
                    print(f"It is HEADS!")
                elif chosen_value.lower() == "t":
                    print(f"It is TAILS!")
                time.sleep(2)

                if players_bet.lower() == chosen_value.lower():
                    print("You won!!!")
                    time.sleep(1)
                    print(f"You are winning {players_money_bet * 2} USD!")
                    time.sleep(1)
                    user.users_wallet += players_money_bet * 2
                    self.wallet -= players_money_bet * 2
                    result = "Win"
                    print(f"You now have {user.users_wallet} USD!")
                    time.sleep(2)

                else:
                    print("You lost! :( ")
                    result = "Loss"
                    time.sleep(2)
                    # money countdown animation

                next_input = input("Do you want to play again? Enter N for no or any other character for yes.\n\n")
                if next_input.lower() == "n":
                    self.games1.choose_game()
                    return
                else:
                    self.start_game(user)

            except ValueError:
                print("Correct your choice. Enter H for Heads or T for Tails")
                continue


flip1 = CoinFlip()

CoinFlip.start_game()