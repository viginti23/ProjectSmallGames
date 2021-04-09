import hashlib
import os
import re
import time
import getpass
from structures.menu_Node import MenuNode
from structures.user_class import User, Admin
from json_data_funcs import read_data_from_users_database, write_data_to_users_database


class RegisterScript:

    def __init__(self):
        pass

    @classmethod
    def email_prompt(cls):
        # Email prompt
        while True:
            print("Enter B to go back.")
            email_input = input("Enter your e-mail:\n")
            if email_input.lower() == 'b':
                return MenuNode.current_node()
            if cls.email_is_valid(email_input):
                if cls.email_in_database(email_input):
                    print("\nUser associated with this e-mail address already exists!\n")
                    print("Try logging in instead or recovering your password.")
                    decision = input("""
    
                            Enter M to return to Main Menu.
    
                            Enter E to try with a different e-mail.
                            """)

                    if decision.lower() == "m":
                        return MenuNode.default_node()
                    elif decision.lower() == "e":
                        continue
                else:
                    return email_input
            else:
                print("\nPlease enter valid e-mail address!\n")
                continue

    @classmethod
    def username_is_valid(cls, username):
        # Checking the database for existing user with this username.
        users = read_data_from_users_database()
        all_users = users['users'] + users['admins']
        for user in all_users:
            if user['username'] == username:
                print("\nUser with this username already exists!\n")
                print("Try logging in instead or recovering your password.\n")
                return False
        return True

    @classmethod
    def username_prompt(cls):
        # Username prompt
        while True:
            print("\nEnter B to go back.\n")

            username = input("\nEnter your username:\n")

            if username.lower() == 'b':
                return MenuNode.previous_node()
            elif cls.username_is_valid(username):
                return username
            else:
                print("Please enter a new username.\n")
                continue

    @classmethod
    def email_is_valid(cls, email_address):
        # Validating given email address with regex.
        pattern = r'^[\w!#$%&-]+(?:\.[\w!#$%-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}$'
        valid = re.match(pattern, email_address)
        return valid

    @classmethod
    def email_in_database(cls, email_address):
        # Checking the database for existing user with this email address.
        users = read_data_from_users_database()
        all_users = users['admins'] + users['users']
        for user in all_users:
            if email_address.lower() == user['email']:
                return True
        return False

    @classmethod
    def password_prompt(cls, valid_username):
        while True:
            print('''Your password:
                    - should be longer than 6 characters;
                    - should contain at least one digit;
                    - should not contain the word "password" in any case;
                    - should not be the same as your username;
                    - should contain at least 3 different characters.
        ''')

            password1 = getpass.getpass("Please enter your password:\n")
            if cls.is_acceptable_password(valid_username, password1):
                password2 = getpass.getpass("Please enter your password once again.\n")
                if password2 != password1:
                    print("The passwords are different, please type them again!\n")
                    continue
                else:
                    # returns pair (salt, key)
                    return cls.hash_pw(password1)

    @classmethod
    def stop_watch_to_main_menu(cls, sec):
        while sec:
            minn, secc = divmod(sec, 60)
            timer = '{:02d}:{:02d}'.format(minn, secc)
            print(timer, end='\r')
            time.sleep(1)
            sec -= 1
        # MenuNode.current_node()

    @classmethod
    def is_acceptable_password(cls, password, a):
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

    @classmethod
    def hash_pw(cls, pw):
        # Hashing function.
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256',
                                  pw.encode('utf-8'),  # converts given password to bytes
                                  salt,
                                  100000)
        return salt, key  # both bytes type

    @classmethod
    def register_script(cls):
        print("\nThank you for registering!\n")
        # time.sleep(1)
        valid_email = cls.email_prompt()
        valid_username = cls.username_prompt()
        print(f'''
                            \nWelcome {valid_username}!\n
        ''')

        valid_salt, valid_key = cls.password_prompt(valid_username)

        adm = getpass.getpass("\nPress enter to continue or type the admin access password to gain admin powers and "
                              "permissions.\n")

        all_users = read_data_from_users_database()
        if adm == 'admin':  # TODO hash and database export/import?
            new_admin = Admin(email=valid_email, username=valid_username, key=valid_key.hex(),
                              salt=valid_salt.hex())

            print("\nYou are an admin now.\n")

            new_admin_dictionary = new_admin.__dict__
            all_users['admins'].append(new_admin_dictionary)

        else:
            new_user = User(email=valid_email, username=valid_username, key=valid_key.hex(), salt=valid_salt.hex())
            new_user_dictionary = new_user.__dict__
            all_users['users'].append(new_user_dictionary)

        write_data_to_users_database(all_users)

        # TODO sending email to confirm the account
        print("You can now log in.")
        print(f"Returning the the main menu in:")
        cls.stop_watch_to_main_menu(3)
        print('\n')
        return MenuNode.default_node()

# RegisterScript.register_script()