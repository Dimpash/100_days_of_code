import requests
import auth_data
import datetime as dt
MY_LATITUDE = 55.184807
MY_LONGITUDE = 30.201622

params = {
    'lat': MY_LATITUDE,
    'lng': MY_LONGITUDE,
    'formatted': 0
}


proxies = {
        'http': auth_data.http_proxy,
        'https': auth_data.https_proxy,
    }
response = requests.get(url="https://api.sunrise-sunset.org/json", proxies=proxies, params=params)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise, '===', sunset)