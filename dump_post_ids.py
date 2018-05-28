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
conn.execute('create table if not exists posts (id integer primary key, code text, like_count int, comment_count int, image_url text)')


api = Client(user_name, password)

posts = []
uuid = api.generate_uuid()
results = api.user_feed(user_id)

posts.extend(results.get('items', []))

next_max_id = results.get('next_max_id')
while next_max_id:
    results = api.user_feed(user_id, max_id=next_max_id)
    posts.extend(results.get('items', []))
    next_max_id = results.get('next_max_id')

posts.sort(key=lambda x: x['pk'])

for post in posts:
   caption = post['caption']['text']
   media_id = int(post['pk'])
   code = post['code']
   comment_count = int(post['comment_count'])
   like_count = int(post['like_count'])
   image_url = post['image_versions2']['candidates'][0]['url']
   data = (media_id, code, like_count, comment_count, image_url)
   conn.execute('insert into posts values (?,?,?,?,?)', data)

conn.commit()