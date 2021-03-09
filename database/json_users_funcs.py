import json
from json.decoder import JSONDecodeError
import os


def read_data_from_users_database():
    with open('database/users.json') as data:
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
    with open('database/users.json', 'w') as data:
        json.dump(users_dictionary, data, indent=4)
