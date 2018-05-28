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
conn.execute('create table if not exists post_comments (post_id integer, user_id integer, content text, foreign key(post_id) references posts(id), foreign key(user_id) references users(id))')
conn.execute('create index idx_postcomments_post on post_comments(post_id)')
conn.execute('create index idx_postcomments_user on post_comments(user_id)')

api = Client(user_name, password)
posts = conn.execute('select id from posts')

count = 0
for post in posts:
    post_id = post[0]
    print('Processing post %d' % post_id)
    comments = []
    uuid = api.generate_uuid()
    results = api.media_n_comments(post_id)
    comments.extend(results)
        
    print('%d comments fetched.' % len(comments))
    matching = 0
    for comment in comments:
        user = comment['user']
        pk = int(user['pk'])
        content = comment['text']
        users = conn.execute('select * from users where id = ?', (pk,))
        if users.fetchone():
            matching += 1
            data = (post_id, pk, content)
            conn.execute('insert into post_comments values (?,?,?)', data)
    conn.commit()
    print('%d comments matched.' % matching)
    count += 1
    print('Processed %d posts' % count)


