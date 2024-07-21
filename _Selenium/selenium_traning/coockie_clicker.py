from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime as dt
from pprint import pprint
# New method
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = 'http://orteil.dashnet.org/experiments/cookie/'

# Webdriver setup
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--incognito')
# chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("detach", True)  # This line of code keeps Chrome browser window opened

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(f"{url}")

cookie_tag = driver.find_element(By.ID, 'cookie')

end_time = dt.datetime.now() + dt.timedelta(minutes=1)
# end_time = dt.datetime.now() + dt.timedelta(seconds=10)

while dt.datetime.now() < end_time:
    check_time = dt.datetime.now() + dt.timedelta(seconds=5)
    while dt.datetime.now() < check_time:
        cookie_tag.click()
    money = int(driver.find_element(By.ID, 'money').text)
    store_tag = driver.find_element(By.ID, 'store')
    prices_tags = store_tag.find_elements(By.TAG_NAME, 'div')
    # prices_tags = driver.find_elements(By.CSS_SELECTOR, '#store div')
    max_price = 0
    max_price_id = ''
    for item in prices_tags:
        if item.get_attribute('class') == '':
            price_str = item.find_element(By.TAG_NAME, 'b').text
            price = int(price_str.replace(',', '').split()[-1])
            if (price < money) and (price > max_price):
                max_price = price
                max_price_tag = item
    if max_price > 0:
        max_price_tag.click()

print(driver.find_element(By.ID, 'cps').text)
