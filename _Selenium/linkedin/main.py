from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
import os
import time

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3462972514&f_AL=true&f_T=25169&geoId=101705918&keywords=python&location=Belarus&refresh=true&sortBy=R'

linkedin_user = os.environ.get('LINKEDIN_USER')
linkedin_password = os.environ.get('LINKEDIN_PASSWORD')

# Webdriver setup
chrome_options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')

chrome_options.add_experimental_option("detach", True)  # This line of code keeps Chrome browser window opened

driver = webdriver.Chrome(options=chrome_options)

driver.get(f"{URL}")

login_btn_tag = driver.find_element(By.CSS_SELECTOR, 'header nav div a[data-tracking-control-name=public_jobs_nav-header-signin]')
login_btn_tag.click()

time.sleep(5)

user_name_tag = driver.find_element(By.ID, 'username')
user_name_tag.send_keys(linkedin_user)

password_tag = driver.find_element(By.ID, 'password')
password_tag.send_keys(linkedin_password)

submit_btn_tag = driver.find_element(By.CSS_SELECTOR, 'div button[data-litms-control-urn=login-submit]')
submit_btn_tag.click()

time.sleep(5)

pprint(submit_btn_tag.text)

