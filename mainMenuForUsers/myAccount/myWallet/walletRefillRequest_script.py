from structures.user_class import User
from json_data_funcs import read_data_from_users_database


def wallet_refill():
    users = read_data_from_users_database()
    req = User.user_logged.get_refill_request()
    User.user_logged.send_request_to_admin(req)
    usr_dict = User
    # for u in users['users']:
    #     if u['username'] == User.user_logged.username:
            # del u
            # users['users'].append(
            #     pass
   # write_data_to_users_database(users_dictionary=)