import json
import os.path
import logging
import argparse
import sqlite3
from credentials import *
try:
    from instagram_private_api import (
        Client, __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from instagram_private_api import (
        Client, __version__ as client_version)

conn = sqlite3.connect('instagram.db')
conn.execute('create table if not exists users (id integer primary key, username text, fullname text, points integer)')

api = Client(user_name, password)
print('Dumping followers for user %s' % user_name)

followers = []
uuid = api.generate_uuid()
results = api.user_followers(user_id, uuid, query='')
followers.extend(results.get('users', []))

next_max_id = results.get('next_max_id')
while next_max_id:
    results = api.user_followers(user_id, uuid, max_id=next_max_id)
    followers.extend(results.get('users', []))
    print('%d followers loaded.' % len(followers))

    next_max_id = results.get('next_max_id')


for follower in followers:
    data = (int(follower['pk']), follower['username'], follower['full_name'], 0)
    conn.execute('insert into users values (?,?,?,?)', data)

conn.commit()