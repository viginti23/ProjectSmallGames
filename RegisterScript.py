from LoginMenu import LoginMenu
from User import User
import time
import re
import json
import hashlib
import os

with open('database/users.json') as data:
    db = data.read()

database_dict = json.loads(db)


# Helper functions
# Checks if entered password is acceptable.
def is_acceptable_password(username, a):
    b = "password"
    if b.lower() in a.lower():
        print("Your password can't contain the word 'password' in any case!")
        return False
    diff_chars = []
    if username.lower() in a.lower():
        print("Your password can't contain your username in any case!")
        return False
    for x in a:
        if x not in diff_chars:
            diff_chars.append(x)
    if len(diff_chars) < 3:
        print("Your password must consist of art least 3 different characters!")
        return False
    if len(a) < 9:
        if len(a) <= 6:
            print("Your password must be at least 6 characters long!")
            return False
        num = 0
        for x in a:
            if x.isnumeric():
                num += 1
        if len(a) == num:
            print("Your password can't consist of only numbers!")
            return False
        elif num == 0:
            print("Your password must consist of at least one number!")
    return True


def email_is_valid(email_address):
    # Validating given email address with regex.
    pattern = '^[\w!#$%&\'*+/=?`{|}~^-]+(?:\.[\w!#$%&\'*+/=?`{|}~^-]+)*@(?:[A-Z0-9-]+\.)+[A-Z]{2,6}$'
    valid = re.match(pattern, email_address)
    return valid


def email_in_database(email_address):
    # Checking the database for existing user with this email address.
    for user in database_dict['users']:
        if email_address.lower() == user['email']:
            return True
    return False


def username_is_valid(username):
    for user in database_dict['users']:
        if user.username == username:
            print("User associated with this e-mail address already exists!")
            print("Try logging in instead or recovering your password.")
            return False
    return True


def hash_pw(pw):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', pw.encode('utf-8'), salt, 100000)
    return salt, key


def email_prompt():
    # Email prompt
    while True:
        email_input = input("Enter your e-mail:\n")
        if email_is_valid(email_input):
            if email_in_database(email_input):
                print("User associated with this e-mail address already exists!")
                print("Try logging in instead or recovering your password.")
                decision = input("""

                        Enter L to log in.

                        Enter E to try with a different e-mail.
                        """)

                if decision.lower() == "l":
                    LoginMenu.show_menu_view_and_go_next()
                elif decision.lower() == "e":
                    continue
            else:
                return email_input
        else:
            print("Please enter valid e-mail address!")
            continue


def username_prompt():
    # Username prompt
    while True:
        username = input("Enter your username:\n")
        if username_is_valid(username):
            return username
        else:
            print("Please enter a valid e-mail:\n")
            continue


def password_prompt(valid_username):
    while True:
        print('''Your password:
                                    - should be longer than 6 characters;
                                    - should contain at least one digit;
                                    - should not contain the word "password" in any case;
                                    - should not be the same as your username;
                                    - should contain at least 3 different characters.
    ''')

        password1 = input("Please enter your password:\n")
        if is_acceptable_password(valid_username, password1):
            password2 = input("Please enter your password once again.")
            if password2 != password1:
                print("The passwords are different, please type them again!")
                continue
            else:
                # returns pair (salt, key)
                return hash_pw(password1)


def register_script():
    print("Thank you for registering!")
    time.sleep(1)
    valid_email = email_prompt()
    valid_username = username_prompt()
    print(f'Welcome {valid_username}!')
    time.sleep(1)
    valid_hashed_password = password_prompt(valid_username)
    time.sleep(0.5)
    new_user = User(valid_email, valid_username, valid_hashed_password)
    new_user_json = json.dumps(new_user.__dict__)

    with open('database/users.json', 'a') as datab:
        json.dump(new_user_json, datab)