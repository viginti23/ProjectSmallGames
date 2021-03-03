import hashlib
import json
import os
import re
import time
import codecs
import io
from MenuNode import MenuNode
from User import User
from json.decoder import JSONDecodeError
import base64


def hash_pw(pw):
    # Hashing function.
    salt = os.urandom(32)

    key = hashlib.pbkdf2_hmac('sha256',
                              pw.encode('latin1'),  # converts given password to bytes
                              salt,
                              100000)

    return salt, key  # both bytes type


# valid_salt, valid_key = hash_pw('pass')
# print(valid_salt)
#
# with open('database/users.json') as data:
#     try:
#         if os.stat('database/users.json').st_size != 0:
#             users = json.load(data)
#         else:
#             print("Database is empty.\nCreating new JSON users database template...")
#             users = {'users': []}
#     except JSONDecodeError:
#         print("The JSON database is invalid!\nCreating new JSON users database template...")
#         users = {'users': []}
#
# users['users'].append({'username': 'viginti',
#                        'email': 'zarodm@gmail.com',
#                        'key': '',
#                        'salt': ''})
#
# for user in users['users']:
#     if user['username'] == 'viginti':
#         user['salt'] = valid_salt
#         user['key'] = valid_key
#
# print(users)
# with open('database/users.json', 'w') as data:
#     json.dump(users, data, indent=4)
z = hash_pw('pass')[0]
b = hash_pw('pass')[1]
# print(z)

print(z)
print(b)

hx = z.hex()

print(hx)