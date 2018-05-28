import sqlite3

conn = sqlite3.connect('instagram.db')
print('Updating user points...')
conn.execute('update users set points = (select count(1) from post_comments where user_id = id) + (select count(1) from post_likes where user_id = id)')
conn.commit()

print('Top users: (points = total "comments + likes" on your posts)')
top_users = conn.execute('select username, points from users order by points desc limit 10')
for user in top_users:
    print('%s (%d points)' % (user[0], user[1])) 

ghost_user_count = conn.execute('select count(1) from users where points < 1').fetchall()[0][0]
print('%d ghost users (zero points) found.' % ghost_user_count)
conn.close()
print('Update complete.')