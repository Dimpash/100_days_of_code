from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
import os
import time

URL = 'https://tinder.com/'
WAIT = 5

# Webdriver setup
chrome_options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')

chrome_options.add_experimental_option("detach", True)  # This line of code keeps Chrome browser window opened

driver = webdriver.Chrome(options=chrome_options)

driver.get(f"{URL}")

time.sleep(WAIT)

cookies_tag = driver.find_element(By.XPATH, '//*[@id="t1310926520"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies_tag.click()

log_in_tag = driver.find_element(By.XPATH, '//*[@id="t1310926520"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')
log_in_tag.click()
time.sleep(WAIT)

facebook_tag = driver.find_element(By.XPATH, '//*[@id="t1532266956"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_tag.click()
time.sleep(WAIT)

fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
fb_email = os.getenv('FB_LOGIN')
fb_password = os.getenv('FB_PASSWORD')

email_tag = driver.find_element(By.ID, 'email')
email_tag.send_keys(fb_email)

pass_tag = driver.find_element(By.ID, 'pass')
pass_tag.send_keys(fb_password)

submit_btn_tag = driver.find_element(By.NAME, 'login')
submit_btn_tag.click()

time.sleep(WAIT)

driver.switch_to.window(driver.window_handles[0])

time.sleep(WAIT)

geo_btn_tag = driver.find_element(By.XPATH, '//*[@id="t1532266956"]/main/div/div/div/div[3]/button[1]')
geo_btn_tag.click()

no_message_btn_tag = driver.find_element(By.XPATH, '//*[@id="t1532266956"]/main/div/div/div/div[3]/button[2]')
no_message_btn_tag.click()

div_n = 3

for i in range(0, 5):
    time.sleep(WAIT)
    no_btn_tag = driver.find_element(By.XPATH, f'//*[@id="t1310926520"]/div/div[1]/div/div/main/div/div/div[1]/div/div[{div_n}]/div/div[2]/button')
    no_btn_tag.click()
    div_n = 4
#                                                 //*[@id="t1310926520"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button

# pprint(log_in_tag)

# pprint([x.text + '=' for x in log_in_tag])

