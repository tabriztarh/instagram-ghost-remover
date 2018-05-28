import getpass
import os

print('Please make sure 2FA is disabled before using this script, otherwise it will not work.')
username = raw_input('Enter your Instagram username: ')
password = getpass.getpass('Enter your Instagram password (just type it and press enter, it will not show for security reasons): ')
userid = raw_input('Enter your Instagram user ID (you can find it from https://thumbtube.com/instagram-user-id-finder ): ')
with open('credentials.py', 'w') as credfile:
    credfile.write('user_name = \'%s\'\n' % username)
    credfile.write('password = \'%s\'\n' % password)
    credfile.write('user_id= \'%s\'\n' % userid)

os.system('python dump_follower_ids.py && python dump_post_ids.py && python dump_post_likers.py && python dump_post_commenters.py && python analysis.py')