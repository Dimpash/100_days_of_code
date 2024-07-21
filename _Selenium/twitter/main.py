from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
import os
import time
from internet_speed_twitter_bot import InternetSpeedTwitterBot


DOWNLOAD_SPEED_LIMIT = 110
UPLOAD_SPEED_LIMIT = 100

tw_login = os.getenv('TW_LOGIN')
tw_email = os.getenv('TW_EMAIL')
tw_password = os.getenv('TW_PASSWORD')

tw_bot = InternetSpeedTwitterBot()
download_speed, upload_speed = tw_bot.get_internet_speed()
# print(download_speed, upload_speed)
# download_speed, upload_speed = 50, 60

tweet = ''
if download_speed < DOWNLOAD_SPEED_LIMIT:
    tweet += f' Download speed = {download_speed} is below the speed limit = {DOWNLOAD_SPEED_LIMIT}!'
if upload_speed < UPLOAD_SPEED_LIMIT:
    tweet += f' Upload speed = {upload_speed} is below the speed limit = {UPLOAD_SPEED_LIMIT}!'

if tweet > '':
    message = f'My Internet is slow. {tweet}. This is just a program test.'
    tw_bot.tweet_at_provider(tw_login, tw_email, tw_password, message)


