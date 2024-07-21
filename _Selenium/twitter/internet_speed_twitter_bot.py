from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
import os
import time


SPEED_TEST_URL = 'https://www.speedtest.net/'
TWITTER_URL = 'https://twitter.com/'
WAIT = 3


class InternetSpeedTwitterBot():

    def __init__(self):
        self.download_speed = 0
        self.upload_speed = 0

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)  # This line of code keeps Chrome browser window opened
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get(f"{SPEED_TEST_URL}")

        go_btn_tag = self.driver.find_element(By.CSS_SELECTOR, 'a.js-start-test.test-mode-multi')

        go_btn_tag.click()

        download_speed = 0
        upload_speed = 0
        test_time = 0

        while ((download_speed == 0) and (upload_speed == 0)) or (test_time < 60):
            time.sleep(WAIT)
            test_time += WAIT
            download_speed_tag = go_btn_tag = self.driver.find_element(By.CSS_SELECTOR,
                                                                  'span.result-data-large.number.result-data-value.download-speed')
            if (download_speed == 0) and (download_speed_tag.text != '--'):
                download_speed = float(download_speed_tag.text)
            upload_speed_tag = go_btn_tag = self.driver.find_element(By.CSS_SELECTOR,
                                                                'span.result-data-large.number.result-data-value.upload-speed')
            if (upload_speed == 0) and (upload_speed_tag.text != '--'):
                upload_speed = float(upload_speed_tag.text)

        return download_speed, upload_speed
        # message = ''
        # if download_speed < DOWNLOAD_SPEED_LIMIT:
        #     message += f' Download speed = {download_speed} below speed limit = {DOWNLOAD_SPEED_LIMIT}!'
        # if upload_speed < UPLOAD_SPEED_LIMIT:
        #     message += f' Upload speed = {upload_speed} below speed limit = {UPLOAD_SPEED_LIMIT}!'
        #
        # print(message)

    def tweet_at_provider(self, tw_login, tw_email, tw_password, tweet):
        self.driver.get(f"{TWITTER_URL}")
        login_btn_tag = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        time.sleep(WAIT)
        login_btn_tag.click()
        time.sleep(WAIT)
        login_tag = self.driver.find_element(By.NAME, 'text')
        login_tag.send_keys(tw_login)
        next_btn_tag = self.driver.find_element(By.CSS_SELECTOR,
                                                'div[role=button][style="background-color: rgb(15, 20, 25);"]')
        next_btn_tag.click()
        time.sleep(WAIT)

        password_btn_tag = self.driver.find_element(By.NAME, 'password')
        password_btn_tag.send_keys(tw_password)
        check_password_btn_tag = self.driver.find_element(By.CSS_SELECTOR,
                                                          'div[role=button][data-testid=LoginForm_Login_Button]')
        check_password_btn_tag.click()
        time.sleep(WAIT)

        email_field_tags = self.driver.find_elements(By.CSS_SELECTOR, 'input[inputmode=email]')
        if len(email_field_tags) > 0:
            email_field_tags[0].send_keys(tw_email)
            next_btn_tag = self.driver.find_element(By.CSS_SELECTOR,
                                                    'div[role=button][data-testid=ocfEnterTextNextButton')
            next_btn_tag.click()
            time.sleep(WAIT)

        tweet_btn_tag = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/compose/tweet"]')
        tweet_btn_tag.click()
        time.sleep(WAIT)

        tweet_text_tag = self.driver.find_element(By.CSS_SELECTOR, 'div.draftjs-styles_0 span')
        tweet_text_tag.send_keys(tweet)
        time.sleep(WAIT)

        send_tweet_btn_tag = self.driver.find_element(By.CSS_SELECTOR, 'div[role=button][data-testid=tweetButton]')
        # send_tweet_btn_tag.click()

