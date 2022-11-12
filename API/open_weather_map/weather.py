import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import auth_data

# Vitebsk
# MY_LAT = 55.184807
# MY_LONG = 30.201622

MY_LAT = 42.29
MY_LONG = 41.52

proxies = {
        'http': auth_data.http_proxy,
        'https': auth_data.https_proxy,
    }

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": auth_data.openweathermap_appid,
}


def send_sms():
    # Custom HTTP Class
    # my_request_client = MyRequestClass()
    account_sid = auth_data.twilio_account_sid
    auth_token = auth_data.twilio_auth_token

    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = proxies

    proxy_client = TwilioHttpClient(proxy={'http': proxies['http'], 'https': proxies['https']})

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages.create(
        body="Bring an umbrella",
        from_=auth_data.twilio_phone_number,
        to=auth_data.my_phone_number
    )
    print(message)


def rain_check():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", proxies=proxies, params=parameters)
    # response = requests.get("https://api.openweathermap.org/data/3.0/onecall", proxies=proxies, params=parameters)
    response.raise_for_status()
    data = response.json()
    weather_id = int(data['weather'][0]['id'])
    # print(weather_id)
    if weather_id < 700:
        return True
    else:
        return False

if rain_check():
    send_sms()
    print("The message has been sending")

