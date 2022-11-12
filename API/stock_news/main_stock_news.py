import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import auth_data
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

proxies = {
        'http': auth_data.http_proxy,
        'https': auth_data.https_proxy,
    }

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.
def get_stock_difference():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": auth_data.stock_api_key,
    }

    response = requests.get("https://www.alphavantage.co/query", proxies=proxies, params=stock_parameters)
    response.raise_for_status()
    data = response.json()
    daily_dict = data['Time Series (Daily)']

    # Angela
    data_list = [value for key, value in daily_dict.items()]
    price1 = float(data_list[0]['4. close'])
    price2 = float(data_list[1]['4. close'])


    # date = dt.datetime.now()
    # price1 = 0
    # while price1 == 0:
    #     date += dt.timedelta(days=-1)
    #     date_str = date.strftime('%Y-%m-%d')
    #     if date_str in daily_dict:
    #         price1 = float(daily_dict[date_str]['4. close'])
    #
    # price2 = 0
    # while price2 == 0:
    #     date += dt.timedelta(days=-1)
    #     date_str = date.strftime('%Y-%m-%d')
    #     if date_str in daily_dict:
    #         price2 = float(daily_dict[date_str]['4. close'])

    # print(daily_dict)
    # print(price1)
    # print(price2)
    growth_pc = round((price1 - price2)/price2*100, 1)

    if abs(growth_pc) > 5:
        return True, growth_pc
    else:
        return False, growth_pc

# print(get_stock_difference())


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
def get_news():
    news_parameters = {
        "q": COMPANY_NAME,
        "pageSize": 10,
        "apiKey": auth_data.newsapi_key,
    }

    response = requests.get(NEWS_ENDPOINT, proxies=proxies, params=news_parameters)
    response.raise_for_status()
    data = response.json()
    return data["articles"][:3]

# print(get_news())
#


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
def send_sms(growth_pc, news_list):
    account_sid = auth_data.twilio_account_sid
    auth_token = auth_data.twilio_auth_token

    proxy_client = TwilioHttpClient(proxy={'http': proxies['http'], 'https': proxies['https']})

    client = Client(account_sid, auth_token, http_client=proxy_client)

    msg_bodies = [f"{STOCK}: {growth_pc}%\nHeadline: {item['title']}\nBrief: {item['description']}" for item
                  in news_list]

    for item in msg_bodies:
        print(item)
    #     message = client.messages.create(
    #         body=item,
    #         from_=auth_data.twilio_phone_number,
    #         to=auth_data.my_phone_number
    #     )
    #     print(message)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

big_difference, growth_pc = get_stock_difference()
if big_difference:
    articles = get_news()
    send_sms(growth_pc, articles)

# print(big_difference)
# print(growth_pc)

