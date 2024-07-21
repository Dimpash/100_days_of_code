from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from pprint import pprint

GOOGLE_DOCS_LINK = 'https://docs.google.com/forms/d/1-EEh1jARKe6EU4P0BrYitZrkeIXUu1sXmh1CPDcJDZk/edit#responses'
GOOGLE_FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSevDvRxp7aH7TKb7bcoDFBCfQ3NveF2S9m0RWv5-M6OtLTE0g/viewform?usp=sf_link'
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
# ZILLOW_URL = "https://www.zillow.com/"

# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
# response = requests.get(ZILLOW_URL, headers=header)
# print(response.text)

result_data = [{'address': 'address_1', 'price': 'price_1', 'href': 'href_1'},
               {'address': 'address_2', 'price': 'price_2', 'href': 'href_2'},
               {'address': 'address_3', 'price': 'price_3', 'href': 'href_3'}]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
# chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # Fix for ReCaptcha, but not much help
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) Chrome/84.0.4147.125")
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-GB,en-US;q=0.9,en;q=0.8'})
chrome_options.add_experimental_option("detach", True)  # This line of code keeps Chrome browser window opened
driver = webdriver.Chrome(options=chrome_options)
driver.get(f"{ZILLOW_URL}")

time.sleep(6)

data_tag_list = driver.find_elements(By.CSS_SELECTOR, 'article')
# pprint(data_tag_list)

result_data = []

for tag in data_tag_list:
    href_tag = driver.find_element(By.TAG_NAME, 'a')
    print(href_tag.text)
    href = href_tag.get_attribute('href')
    price_tag = driver.find_element(By.CSS_SELECTOR, 'span')
    price = price_tag.text
    address_tag = driver.find_element(By.CSS_SELECTOR, 'address')
    address = address_tag.text
    result_data.append({'address': address, 'price': price, 'href': href})

pprint(result_data)


driver.get(f"{GOOGLE_FORM_LINK}")
time.sleep(3)

for item in result_data:
    tag = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    tag.send_keys(item['address'])
    tag = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    tag.send_keys(item['price'])
    tag = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    tag.send_keys(item['href'])

    tag = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    tag.click()
    time.sleep(3)

    tag = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    tag.click()
    time.sleep(3)

# driver.get(f"{GOOGLE_DOCS_LINK}")
# time.sleep(3)

driver.close()


