import json
from json.decoder import JSONDecodeError
from MenuNode import MenuNode
from User import User
import time as t
import os
import hashlib
import random

with open('database/users.json') as users:
    try:
        users = json.load(users)
    except JSONDecodeError:
        users = {'users': []}


# current_user = None
def hash_pw(pw):
    # Hashing function.
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', pw.encode('utf-8'), salt, 100000)
    return salt, key
# def forgot_password():

def stop_watch_to_main_menu(sec):
    while sec:
        minn, secc = divmod(sec, 60)
        timer = '{:02d}:{:02d}'.format(minn, secc)
        print(timer, end='\r')
        t.sleep(1)
        sec -= 1
    MenuNode.current_node()

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
    valid_salt, valid_key = hash_pw(new_password)
    new_password = valid_salt+valid_key
    for u in users['users']:
        if u['username'] == usr.username:
            u['password'] = new_password
    with open('database/users.json', ) as reset_pw_users:
        json.dump(users, reset_pw_users, indent=4)
    return

def login_script():
    current_user = None
    while True:
        username_or_email = input("Enter your e-mail or username:\n")

        for user in users['users']:
            if not (user['username'] == username_or_email or user['email'] == username_or_email):
                print('Username not found!\nRegister first.')
                t.sleep(1)
                decision = input(f'Return to {MenuNode.default_node.name} in {stop_watch_to_main_menu(10)} seconds'
                                 f'.\nEnter anything to try logging in again.\n Enter'
                                 f'B to return to {MenuNode.default_node.name}.')
                if decision.lower() == 'b':
                    MenuNode.current_node()
                else:
                    continue
            else:
                print('Username found!')
                if current_user is None:
                    current_user = user
                break
        break

    count = 0
    while count < 4:
        password = input("Enter your password:\n")
        if str(hash_pw(password)) == current_user['password']:
            User.user_logged = current_user
            print("You are now logged in!")
            break
        else:
            print('Password incorrect.\n')
            count += 1
            continue
    if count >= 3:
        print("Too many tries. Please use 'Forget password' to regain access to your account.")
        password_reset(current_user)
        MenuNode.default_node()
