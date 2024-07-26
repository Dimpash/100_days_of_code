from bs4 import BeautifulSoup
import requests
from pprint import pprint

from selenium import webdriver

URL = "https://www.empireonline.com/movies/features/best-movies-2022/"

# webdriver setup
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get(URL)
web_page = driver.page_source
# print(web_page)

soup = BeautifulSoup(web_page, "html.parser")

sel = soup.select(selector="h3.jsx-4245974604")
movies = [tag.getText().split('. ', maxsplit=1) for tag in sel]
for item in movies:
    item[0] = int(item[0])
movies.sort()
# pprint(movies)

with open('movies.txt', 'w') as file:
    for item in movies:
        file.write(f"{item[0]}. {item[1]}\n")



# # ycombinator
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# print(yc_web_page)
#
# res2 = soup.select(selector="span.titleline > a")
# pprint(res2)
#
# for tag in res2:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# res3 = soup.select(selector="span.score")
# for tag in res3:
#     print(tag.getText())
#










# res3 = soup.select(selector="td.title")
# pprint(res3)

# for tag in res1:
#     new_soup = BeautifulSoup(tag, "html.parser")
    # anchor = new_soup.find(name="a")
    # href = new_soup.get("href")
    # print(href, "===", anchor)










# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# pprint(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.get("href"))