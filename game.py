import json
from json.decoder import JSONDecodeError
import os
import sys
import time
from datetime import datetime


class Game:
    games_list = []

    # a każda gra będzie miała swoje game_id
    def __init__(self, name, user, dat):
        self.name = name
        self.user = user

    def run_game(self):
        date_played = datetime.now()
        game_id = None
