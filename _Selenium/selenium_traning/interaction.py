from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint


def wikipedia_work():
    url = 'https://en.wikipedia.org/wiki/Main_Page'

    # Webdriver setup
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--headless')
    # chrome_options.add_experimental_option("detach", True) # This line of code keeps Chrome browser window opened

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(f"{url}")

    # tag = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[@title="Special:Statistics"]')
    tag = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
    print(tag.text)

def appbrewery_work():
    url = 'https://www.appbrewery.co/p/newsletter'

    # Webdriver setup
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--incognito')
    # chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("detach", True)  # This line of code keeps Chrome browser window opened

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(f"{url}")

    div_tag = driver.find_element(By.ID, 'profile-form-fields')
    email_input = div_tag.find_element(By.ID, 'member_email')
    email_input.send_keys('ddddddd.eeeeeee@mail.ry')
    submit_input = div_tag.find_element(By.NAME, 'commit')
    submit_input.send_keys(Keys.ENTER)


appbrewery_work()
