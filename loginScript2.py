import json
from json.decoder import JSONDecodeError
from menuNode import MenuNode
from user import User
from mainMenu_forUsers import MainMenuForUsers
import time
import os
import hashlib
import random
from database.json_users_funcs import read_data_from_users_database, write_data_to_users_database


def stop_watch_to_default_node(sec):
    while sec:
        minn, secc = divmod(sec, 60)
        timer = '{:02d}:{:02d}'.format(minn, secc)
        print(timer, end='\r')
        time.sleep(1)
        sec -= 1
    MenuNode.default_node()


def password_reset(usr):
    random_string = ''
    for _ in range(10):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    new_password = random_string
    salt = bytes.fromhex(usr.salt)
    new_key = hashlib.pbkdf2_hmac('sha256',
                                  new_password.encode('utf8'),
                                  salt,
                                  100000)
    users = read_data_from_users_database()
    for u in users['users']:
        if u['username'] == usr.username:
            u['key'] = new_key.hex()
    write_data_to_users_database(users)
    print('Password has been reset!')


def login_script():
    # Searching for user in database
    users = read_data_from_users_database()
    identified_user = None
    while not identified_user:
        print('\n\nEnter R to return to main menu.')
        username_input = input('\nEnter your username or e-mail:\n')
        if username_input.lower() == 'r':
            MenuNode.current_node()
        for user in users['users']:
            if username_input == user['username'] or username_input == user['email']:
                identified_user = User(dictionary=user)  # Our currently most used user is in Python class type.
                # if not dict_: ---> ---> identified_user.dictionary
                #     dict_ = user
                print(type(user))
                print("\nUser found!")
                break
        if not identified_user:
            print("\nThis user does not exist. Try different username or register instead.")
            time.sleep(2)
            login_script()

    # Verifying password
    count = 0
    while count < 4:
        print('\n\nEnter R to return to main menu.')
        password_to_check = input("\nEnter your password:\n")
        if password_to_check.lower() == 'r':
            MenuNode.current_node()
        salt = bytes.fromhex(identified_user.salt)
        new_key = hashlib.pbkdf2_hmac('sha256',
                                      password_to_check.encode('utf-8'),
                                      salt,
                                      100000)
        if new_key.hex() == identified_user.key:
            print("\nPassword correct.\n")
            User.user_logged = identified_user
            break
        else:
            print('\nPassword incorrect. Try again.\n')
            count += 1
    if count >= 3:
        print("\nToo many tries. Please use 'Forget password' to regain access to your account.\n")
        print("\nResetting password...\n")
        # password_reset(identified_user)
        print(f'Returning to {MenuNode.default_node.name} in:')
        stop_watch_to_default_node(3)
    else:
        MenuNode.default_node = MainMenuForUsers
        MenuNode.current_node = MainMenuForUsers
        MenuNode.current_node()
