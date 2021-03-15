import json
from json.decoder import JSONDecodeError
import os


# User class functions
def read_data_from_users_database():
    with open("database/users.json") as data:
        try:
            if os.stat('database/users.json').st_size != 0:
                return json.load(data)
            # else:
            #     print("Database is empty.\nCreating new JSON users database template...")
            #     users = {'users': []}
        except JSONDecodeError:
            print("The JSON database is invalid!\nCreating new JSON users database template...")
            return {'users': []}


def write_data_to_users_database(users_dictionary):
    with open("database/users.json", "w") as data:
        json.dump(users_dictionary, data, indent=4)


# Games class functions
def read_data_from_games_database():
    with open("database/games.json") as data:
        try:
            if os.stat('database/games.json').st_size != 0:
                return json.load(data)
            else:
                print("Database is empty.\nCreating new JSON games database template...")
                return {'games': []}
        except JSONDecodeError:
            print("The JSON database is invalid!\nCreating new JSON games database template...")
            return {'games': []}


def write_data_to_games_database(games_dictionary):
    with open("database/games.json", "w") as data:
        json.dump(games_dictionary, data, indent=4)
