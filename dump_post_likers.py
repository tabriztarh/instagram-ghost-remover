import json
import os.path
import logging
import argparse
import sqlite3
from credentials import user_name, password

try:
    from instagram_private_api import (
        Client, __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from instagram_private_api import (
        Client, __version__ as client_version)

conn = sqlite3.connect('instagram.db')
conn.execute('create table if not exists post_likes (post_id integer, user_id integer, foreign key(post_id) references posts(id), foreign key(user_id) references users(id))')
conn.execute('create index idx_postlikes_post on post_likes(post_id)')
conn.execute('create index idx_postlikes_user on post_likes(user_id)')

api = Client(user_name, password)

posts = conn.execute('select id from posts')

count = 0
for post in posts:
    post_id = post[0]
    print('Processing post %d' % post_id)
    likes = []
    uuid = api.generate_uuid()
    results = api.media_likers(post_id)
    likes.extend(results.get('users', []))

    next_max_id = results.get('next_max_id')
    while next_max_id:
        results = api.media_likers(post_id, max_id=next_max_id)
        posts.extend(results.get('users', []))
        next_max_id = results.get('next_max_id')
        
    print('%d likes fetched.' % len(likes))
    matching = 0
    for like in likes:
        pk = int(like['pk'])
        users = conn.execute('select * from users where id = ?', (pk,))
        if users.fetchone():
            matching += 1
            data = (post_id, pk)
            conn.execute('insert into post_likes values (?,?)', data)
        conn.commit()
    print('%d users matched.' % matching)
    count += 1
    print('Processed %d posts' % count)


