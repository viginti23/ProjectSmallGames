import hashlib
import json
import os
import re
import time
from structures.menu_Node import MenuNode
from structures.user_class import User
from guestMenu.Register.json_users_funcs import read_data_from_users_database

users = read_data_from_users_database()


# Helper functions
def email_prompt():
    # Email prompt
    while True:
        email_input = input("Enter your e-mail:\n")
        if email_is_valid(email_input):
            if email_in_database(email_input):
                print("\nUser associated with this e-mail address already exists!\n")
                print("Try logging in instead or recovering your password.")
                decision = input("""

                        Enter M to return to Main mainMenuForUsers

                        Enter E to try with a different e-mail.
                        """)

                if decision.lower() == "m":
                    MenuNode.default_node()
                elif decision.lower() == "e":
                    continue
            else:
                return email_input
        else:
            print("\nPlease enter valid e-mail address!\n")
            continue


def username_prompt():
    # Username prompt
    while True:
        username = input("\nEnter your username:\n")
        if username_is_valid(username):
            return username
        else:
            print("Please enter a new username.\n")
            continue


def email_is_valid(email_address):
    # Validating given email address with regex.
    pattern = r'^[\w!#$%&-]+(?:\.[\w!#$%-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}$'
    valid = re.match(pattern, email_address)
    return valid


def email_in_database(email_address):
    # Checking the database for existing user with this email address.
    for user in users['users']:
        if email_address.lower() == user['email']:
            return True
    return False


def username_is_valid(username):
    # Checking the database for existing user with this username.
    for user in users['users']:
        if user['username'] == username:
            print("\nUser with this username already exists!\n")
            print("Try logging in instead or recovering your password.\n")
            return False
    return True


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
            password2 = input("Please enter your password once again.\n")
            if password2 != password1:
                print("The passwords are different, please type them again!\n")
                continue
            else:
                # returns pair (salt, key)
                return hash_pw(password1)


def stop_watch_to_main_menu(sec):
    while sec:
        minn, secc = divmod(sec, 60)
        timer = '{:02d}:{:02d}'.format(minn, secc)
        print(timer, end='\r')
        time.sleep(1)
        sec -= 1
    # MenuNode.current_node()


def is_acceptable_password(password, a):
    # Checks if entered password is acceptable.
    b = "password"
    if b.lower() in a.lower():
        print("Your password can't contain the word 'password' in any case!")
        return False
    diff_chars = []
    if password.lower() in a.lower():
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


def hash_pw(pw):
    # Hashing function.
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256',
                              pw.encode('utf-8'),  # converts given password to bytes
                              salt,
                              100000)
    return salt, key  # both bytes type


def register_script():
    print("\nThank you for registering!\n")
    # time.sleep(1)
    valid_email = email_prompt()
    valid_username = username_prompt()
    print(f'''
                        \nWelcome {valid_username}!\n
    ''')
    valid_salt, valid_key = password_prompt(valid_username)

    new_user = User(email=valid_email,
                    username=valid_username, key=valid_key.hex(),
                    salt=valid_salt.hex())

    new_user_dictionary = new_user.__dict__
    users['users'].append(new_user_dictionary)
    with open('database/users.json', 'w', encoding='utf8') as usr_file:
        json.dump(users, usr_file, indent=4)
    User.n += 1
    # # TODO sending email to confirm the account
    print("You can now log in.")
    print(f"Returning the the main menu in:")
    stop_watch_to_main_menu(3)
    print('\n')
    MenuNode.default_node()
