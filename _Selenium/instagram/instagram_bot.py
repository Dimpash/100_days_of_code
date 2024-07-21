from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import time


INSTAGRAM_URL = 'https://www.instagram.com/'


class InstagramBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)  # This line of code keeps Chrome browser window opened
        self.driver = webdriver.Chrome(options=chrome_options)
        self.followers_tag_list = []
        self.followers_list = []
        self.delay = 5
        self.follow_delay = 2

    def auth(self, insta_username, insta_password):
        self.driver.get(f"{INSTAGRAM_URL}")

        time.sleep(self.delay)

        username_tag = self.driver.find_element(By.NAME, 'username')
        username_tag.send_keys(insta_username)

        password_tag = self.driver.find_element(By.NAME, 'password')
        password_tag.send_keys(insta_password)

        submit_btn_tag = self.driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
        submit_btn_tag.click()
        time.sleep(self.delay)

        splash_screen_key = True
        while splash_screen_key:
            btn_tags = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            not_now_btn_tag = None
            for tag in btn_tags:
                if tag.text == 'Не сейчас':
                    not_now_btn_tag = tag
                    break
            if not_now_btn_tag is None:
                splash_screen_key = False
            else:
                not_now_btn_tag.click()
                time.sleep(self.delay)

    def get_followers_list(self, username, max_followers=200):
        self.driver.get(f"{INSTAGRAM_URL}/{username}")
        time.sleep(self.delay)

        followers_link_tag = self.driver.find_element(By.CSS_SELECTOR, f'a[href="/{username}/followers/"]')
        followers_link_tag.click()
        time.sleep(self.delay)

        # Do scrolling
        followers_count = 0
        do_scroll = True

        while do_scroll and (followers_count < max_followers):
            self.followers_tag_list = self.driver.find_elements(By.CSS_SELECTOR,
                                                           'div[class="_aano"] > div > div > div')
            if followers_count < len(self.followers_tag_list):
                followers_count = len(self.followers_tag_list)
                bar = self.followers_tag_list[0].find_element(By.CSS_SELECTOR, 'span a[role=link]')
                bar.send_keys(Keys.END)
                time.sleep(self.delay)
            else:
                do_scroll = False

        #  Get follower info
        for tag in self.followers_tag_list:
            link_tag = tag.find_element(By.CSS_SELECTOR, 'span a[role=link]')
            follower = {'link': link_tag.get_attribute('href')}
            follower['username'] = follower['link'].split(sep='/')[-2]

            btn_tags = tag.find_elements(By.CSS_SELECTOR, 'button')
            if len(btn_tags) == 0:
                follower['following'] = True
            elif btn_tags[0].find_element(By.CSS_SELECTOR, 'div > div').text in ['Following', 'Подписки']:
                follower['following'] = True
            else:
                follower['following'] = False
                follower['follow_btn'] = btn_tags[0]
                # follower['following'] = btn_tags[0].find_element(By.CSS_SELECTOR, 'div > div').text in ['Following', 'Подписки']

            name_tags = tag.find_elements(By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(2) > div')
            if len(name_tags) > 0:
                follower['name'] = name_tags[0].text
            else:
                follower['name'] = ''

            self.followers_list.append(follower)

        # print(followers_count)
        #
        # pprint(followers_list)
        # print(len(followers_list))

    def follow(self, max_follows=0):
        follows_count = 0
        for follower in self.followers_list:
            if not follower['following']:
                follower['follow_btn'].click()
                time.sleep(self.follow_delay)
                follows_count += 1
                if follows_count == max_follows:
                    break
        return follows_count



