import random
import time
import turtle
from datetime import datetime
from structures.user_class import User
from structures.game_class import Game
from structures.menu_Node import MenuNode
import json_data_funcs


class TurtleRace(Game):
    games = json_data_funcs.read_data_from_games_database()

    users = json_data_funcs.read_data_from_users_database()

    # Window setup variables
    WIDTH, HEIGHT = 700, 700

    def __init__(self):
        super().__init__(name='Turtle Race')

    def how_many_turtles(self):
        while True:
            num = input("Enter number of turtles (2 - 10):\n"
                        "The greater the number, the higher your possible win is.\n"
                        "Your bet is multiplied by the racers number.\n")
            try:
                num = int(num)
            except ValueError:
                print("Enter valid input.")
                continue
            if num not in range(2, 11):
                print("Number not in the range.")
                continue
            else:
                racers = num
            return racers

    def screen_setup(self):
        screen = turtle.Screen()
        screen.setup(self.WIDTH, self.HEIGHT)
        screen.title("Turtles Race!")

    def create_turtles(self, colors):
        turtles = []
        spacex = self.WIDTH // (len(colors) + 1)
        for i, color in enumerate(colors):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.left(90)
            racer.penup()
            racer.setpos(-self.WIDTH // 2 + (i + 1) * spacex, -self.HEIGHT // 2 + 25)
            racer.pendown()
            turtles.append(racer)
        return turtles

    def race(self, colors):
        turtles = self.create_turtles(colors)

        while True:
            for i, racer in enumerate(turtles):
                distance = random.randrange(1, 20)
                racer.forward(distance)

                x, y = racer.pos()

                if y >= self.HEIGHT // 2 - 10:  # Finish line at +190
                    return colors[i]

    def start_game(self):
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

            players_money_bet = self.getting_players_bet(playing_user)
            racers = self.how_many_turtles()
            COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'cyan', 'pink', 'purple', 'orange', 'brown']
            random.shuffle(COLORS)
            colors = COLORS[:int(racers)]
            for color in colors:
                print(f"\n{color}\n")
            while True:
                inp = input("\n\nWhich turtle will win the race?\nEnter your type now!\n\n")
                if inp not in colors:
                    print("Invalid type!")
                    continue
                break
            turtle.Screen().clear()

            self.screen_setup()

            winner = self.race(colors)
            if inp.lower() == winner.lower():
                print(f'The winner is {winner}!\n'
                      f'You won!!!\n')
                current_session_results.append(
                    ['W', f"Money bet: {players_money_bet}",
                     f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])
                playing_user.wallet += len(colors) * players_money_bet
                self.register -= len(colors) * players_money_bet
                score += len(colors) * players_money_bet

            else:
                print(f'The winner is {winner}!\n'
                      f'You lost! :( \n')

                playing_user.wallet -= players_money_bet
                self.register += players_money_bet
                score -= players_money_bet
                current_session_results.append(
                    ['L', f"Money bet: {players_money_bet}",
                     f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])

            print(f"\nSession's score: {score}.")
            print(f"\nCurrent's session results: {current_session_results}.")
            print(f"\nYour wallet's status: {playing_user.wallet}.")
            time.sleep(5)
            turtle.Screen().bye()

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


