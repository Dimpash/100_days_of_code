from pprint import pprint
import os
from instagram_bot import InstagramBot


insta_username = os.getenv('INSTA_USERNAME')
# tw_email = os.getenv('TW_EMAIL')
insta_password = os.getenv('INSTA_PASSWORD')

insta_bot = InstagramBot()
insta_bot.auth(insta_username=insta_username, insta_password=insta_password)

insta_bot.get_followers_list(username='kasatka0154', max_followers=20)
follows_count = insta_bot.follow(max_follows=3)


