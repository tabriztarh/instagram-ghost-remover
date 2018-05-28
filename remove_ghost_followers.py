import json
import os.path
import logging
import argparse
import sqlite3
import random
from credentials import user_name, password
from time import sleep

try:
    from instagram_private_api import (
        Client, __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from instagram_private_api import (
        Client, __version__ as client_version)

conn = sqlite3.connect('instagram.db')
all_users = conn.execute('select * from users').fetchall()
print('Total users in database: %d' % len(all_users))

users_to_delete = conn.execute('select * from users where points < 1 order by length(username) desc').fetchall()
print('Users to remove: %d' % len(users_to_delete))

if len(all_users) == len(users_to_delete):
    print('All users have zero points. Please run analysis first.')
    exit


api = Client(user_name, password)
print('Logged in as %s to remove %d followers.' % (user_name, len(users_to_delete)))
for user in users_to_delete:
    pk = user[0]
    username = user[1]
    api.friendships_block(pk)
    print('Blocked %s' % username)
    api.friendships_unblock(pk)
    print('Unblocked %s. They are no longer a follower.' % username)
    conn.execute('delete from users where id = ?', (pk,))
    conn.commit()
    random_delay = 15 + random.random() * 20 
    sleep(random_delay) # wait between 15 to 35 seconds