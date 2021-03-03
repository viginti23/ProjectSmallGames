import json
from json.decoder import JSONDecodeError
from MenuNode import MenuNode
from User import User
from MainMenuForLoggedIn import MainMenuForLoggedIn
import time
import os
import hashlib
import random

# if __name__ == '__main__':
with open('database/users.json') as data:
    try:
        if os.stat('database/users.json').st_size != 0:
            users = json.load(data)
        # else:
        #     print("Database is empty.\nCreating new JSON users database template...")
        #     users = {'users': []}
    except JSONDecodeError:
        print("The JSON database is invalid!\nCreating new JSON users database template...")
        users = {'users': []}


def stop_watch_to_default_node(sec):
    while sec:
        minn, secc = divmod(sec, 60)
        timer = '{:02d}:{:02d}'.format(minn, secc)
        # print(f'\nReturning to {MenuNode.default_node.name} in:')
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
    for u in users['users']:
        if u['username'] == usr.username:
            u['key'] = new_key.hex()
    with open('database/users.json', 'w') as reset_pw_users:
        json.dump(users, reset_pw_users, indent=4)
    return


def login_script():
    # Searching user in database
    identified_user = None
    while identified_user is None:
        username_input = input('Enter your username or e-mail:\n')
        for user in users['users']:
            if user['username'] == username_input or user['email'] == username_input:
                identified_user = User(dictionary=user)
                print("\nUser found!")
                break
            # print("This user does not exist. Try different username or register instead.")

    # Verifying password
    count = 0
    while count < 4:
        password_to_check = input("\nEnter your password:\n")
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
        password_reset(identified_user)
    MenuNode.default_node = MainMenuForLoggedIn
    print(f'Returning to {MenuNode.default_node.name} in:')
    stop_watch_to_default_node(5)
