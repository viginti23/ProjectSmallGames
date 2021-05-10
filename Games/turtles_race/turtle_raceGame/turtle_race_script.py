import os
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
    racers = 0
    # Window setup variables
    WIDTH, HEIGHT = 700, 700

    def __init__(self):
        super().__init__(name='Turtle Race')
        self.score = 0
        self.current_session_results = []

    def how_many_turtles(self):
        while True:
            num = input("Enter number of turtles (2 - 10):\n"
                        "The greater the number, the higher your possible win is.\n"
                        "Your bet is multiplied by the racers number.\n")
            try:
                num = int(num)
                TurtleRace.racers = num
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
        screen.setup(self.WIDTH, self.HEIGHT, startx=0, starty=0)
        screen.title("Turtles Race!")
        turtle.TurtleScreen._RUNNING = True

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

    def evaluating_results(self, players_choice, drawn_value, players_money_bet, playing_user):
        if players_choice.lower() == drawn_value.lower():
            print(f'The winner is {drawn_value}!\n'
                  f'You won!!!\n')
            self.current_session_results.append(
                ['W', f"Money bet: {players_money_bet}",
                 f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])
            playing_user.wallet += (TurtleRace.racers * players_money_bet) - players_money_bet
            self.register -= (TurtleRace.racers * players_money_bet) - players_money_bet
            self.score += (TurtleRace.racers * players_money_bet) - players_money_bet

        else:
            print(f'The winner is {drawn_value}!\n'
                  f'You lost! :( \n')

            playing_user.wallet -= players_money_bet
            self.register += players_money_bet
            self.score -= players_money_bet
            self.current_session_results.append(
                ['L', f"Money bet: {players_money_bet}",
                 f"Date: {datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')}"])

    def game(self, playing_user):

        # while True:
        self.not_enough_money(playing_user.wallet)

        # Getting player's points bet
        players_money_bet = self.getting_players_bet(playing_user)

        # Ten different colors referring to max number of racers.
        COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'cyan', 'pink', 'purple', 'orange', 'brown']
        random.shuffle(COLORS)

        # Creating the racers.
        racers = self.how_many_turtles()

        colors = COLORS[:int(racers)]

        chosen_turtle = ''
        while True:
            for i, color in enumerate(colors):
                print(f"\n{i+1}| {color}\n")

            try:
                players_choice = input("\n\nWhich turtle will win the race?\nEnter your type number now!\n\n")
                players_choice = int(players_choice)
                try:
                    chosen_turtle = colors[players_choice-1]
                    break
                except IndexError:
                    print("\nInvalid input, try typing numbers in the correct range.\n")
                    time.sleep(1)
                    continue
            except ValueError:
                print("\nInvalid input, try typing numbers.\n")
                time.sleep(1)
                continue
        # turtle.Screen().clear()

        self.screen_setup()

        # Race itself.
        winner = self.race(colors)
        os.system('clear')

        # Closing the race window.
        inp = input("\n\n\t\t\tPress Enter to close the window.\n\n")
        turtle.Screen().bye()
        turtle.Screen._RUNNING = True

        return chosen_turtle, winner, players_money_bet
