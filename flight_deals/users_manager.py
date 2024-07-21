import requests
import os
from pprint import pprint

class UsersManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/d57a1b9ad4ed64e22745313802ffb155/myFlightDeals/users"
        self.SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
        self.sheety_headers = {"Authorization": f"Bearer {self.SHEETY_TOKEN}"}
        self.data = []

    def get_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        self.data = response.json()["users"]
        # print(self.data)
        return self.data

    def add_user(self):
        first_name = input("Input your first name: ")
        last_name = input("Input your last name: ")
        email = input("Input your email: ")
        if email != input("Type your email again: "):
            next_step = input("Email are not equal. Operation failed. Do you want to repeat (y/n)? ")
        else:
            url = f"{self.sheety_endpoint}"
            request_json = {'user': {"firstName": first_name,
                                     "lastName": last_name,
                                     "email": email}
                            }
            response = requests.post(url=url, json=request_json, headers=self.sheety_headers)
            # pprint(response.text)
            next_step = input("Success. Your email has been added. Do you want to add new email (y/n)? ")
        return next_step



