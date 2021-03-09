import json
from json.decoder import JSONDecodeError
import os
import sys
import time
from datetime import datetime


class Game:
    games_list = []

    def __init__(self, name, user):
        self.name = name
        self.user = user
        Game.games_list.append(self)

    def __repr__(self):
        return self.name

    def __call__(self):
        return self

    def run_game(self):
        date_played = datetime.now()
        game_id = None

