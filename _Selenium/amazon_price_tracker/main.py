from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import lxml
from pprint import pprint
import os

def sending_email(message_text):
    # This function uses send_message metod instead sendmail
    smtp_user = os.environ.get('MY_EMAIL')
    smtp_password = os.environ.get('MY_PASSWORD')
    destination_email = os.environ.get('destination_email')

    # Define message params
    msg = EmailMessage()
    msg.set_content(message_text)
    msg['Subject'] = 'Amazon info'
    msg['From'] = smtp_user
    msg['To'] = destination_email

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=smtp_user, password=smtp_password)
        connection.send_message(msg)
        # connection.sendmail(from_addr=smtp_user, to_addrs=destination_email, msg=message)

# URL = 'https://www.amazon.com/ASUS-Display-i7-12650H-Thunderbolt-FX517ZM-AS73/dp/B09RMH9B6F/ref=sr_1_14?fst=as%3Aoff&pd_rd_r=bb85b1c9-9442-4e91-b2de-5c1e6b46945b&pd_rd_w=A50Fr&pd_rd_wg=Nz76W&pf_rd_p=5b7fc375-ab40-4cc0-8c62-01d4de8b648d&pf_rd_r=0VKT969466MG949C1RPA&qid=1673697392&rnid=16225007011&s=computers-intl-ship&sr=1-14&th=1'
URL = 'https://www.amazon.com/Lenovo-Display-Storage-Graphics-Graphite/dp/B09YWM1CM1/ref=sr_1_23?fst=as%3Aoff&pd_rd_r=bb85b1c9-9442-4e91-b2de-5c1e6b46945b&pd_rd_w=A50Fr&pd_rd_wg=Nz76W&pf_rd_p=5b7fc375-ab40-4cc0-8c62-01d4de8b648d&pf_rd_r=0VKT969466MG949C1RPA&qid=1673697392&rnid=16225007011&s=computers-intl-ship&sr=1-23&th=1'

# my_header = {
#     'Request Line': 'GET / HTTP/1.1',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Connection': 'keep-alive',
#     'Host': 'myhttpheader.com',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
# }
#
# response = requests.get(URL, headers=my_header)

# Webdriver setup
options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get(f"{URL}")
web_page = driver.page_source

# Save results into a file with purpose not to do a request every time
# with open('ddd.txt', 'w', encoding="utf-8") as file:
#     file.write(web_page)

# Saved result of the response
# with open('ddd.txt', 'r', encoding="utf-8") as file:
#     web_page = file.read()

soup = BeautifulSoup(web_page, "lxml")
# price_tags = soup.select(selector="div#corePrice_desktop > div > table > tbody > tr > td > span")
price_tags = soup.select(selector="td.a-span12 > span.a-price.a-text-price.a-size-medium.apexPriceToPay > span.a-offscreen")
# pprint(price_tags)
if len(price_tags) > 0:
    price_str = price_tags[0].getText().replace(',', '').replace('$', '')
    price = float(price_str)
else:
    price = 0

max_price = 1000


if price <= 0:
    email_message = 'Attention! Not find data about your item price on Amazon!'
elif price < max_price:
    email_message = f"Low price alert! Only ${price} on Amazon for your item.\n{URL}"
else:
    email_message = ''

if email_message > '':
    sending_email(email_message)

# print(price_str, '===', price)



