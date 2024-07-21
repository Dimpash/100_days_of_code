from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

URL = 'https://www.python.org/'

# Webdriver setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--headless')
# chrome_options.add_experimental_option("detach", True) # This line of code keeps Chrome browser window opened
# pprint(chrome_options)

# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)
#
driver.get(f"{URL}")

# CSS_SELECTOR method
tags = driver.find_elements(By.CSS_SELECTOR, "div.event-widget > div.shrubbery > ul.menu > li ")

# XPATH method
# tags = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
# pprint(tags)

events = {}
i = 0
for item in tags:
    event_time = item.find_element(By.TAG_NAME, 'time').text
    event_name = item.find_element(By.TAG_NAME, 'a').text
    events[i] = {'time': event_time, 'name': event_name}
    i += 1

pprint(events)

# driver.quit()  # Close browser window. Don't necessary if detach = False
