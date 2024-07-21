import requests
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/d57a1b9ad4ed64e22745313802ffb155/myFlightDeals/prices"
        self.SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
        self.sheety_headers = {"Authorization": f"Bearer {self.SHEETY_TOKEN}"}
        self.data = []

    def get_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        self.data = response.json()["prices"]
        # print(self.data)
        return self.data

    def save_iata_code(self, id, iata_code):
        url = f"{self.sheety_endpoint}/{id}"
        request_config = {'price': {"iataCode": iata_code}
                          }
        response = requests.put(url=url, json=request_config, headers=self.sheety_headers)

