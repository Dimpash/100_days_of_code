import requests
import datetime as dt
import os
from pprint import pprint

from flight_data import FlightData

TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY')

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_endpoint = "https://api.tequila.kiwi.com"
        self.apikey = TEQUILA_API_KEY
        self.api_headers = {"apikey": f"{self.apikey}"}
        self.fly_from = 'LON'
        self.date_from = (dt.datetime.now() + dt.timedelta(days=1)).strftime('%d/%m/%Y')
        self.date_to = (dt.datetime.now() + dt.timedelta(days=180)).strftime('%d/%m/%Y')
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.curr = 'GBP'
        self.flight_type = 'round'
        self.max_stopovers = 1
        self.one_for_city = '1'

    def get_iata_code(self, city_name):
        url = f"{self.api_endpoint}/locations/query"
        request_params = {"term": city_name,
                          "location_types": "city"}
        response = requests.get(url=url, params=request_params, headers=self.api_headers)
        data = response.json()
        return data["locations"][0]['code']

    def get_flight_info(self, to_iata_code, price_to):
        url = f"{self.api_endpoint}/v2/search"
        request_params = {"fly_from": f"city:LON",
                          "fly_to": f"city:{to_iata_code}",
                          "date_from": self.date_from,
                          "date_to": self.date_to,
                          "flight_type":self.flight_type,
                          "nights_in_dst_from": self.nights_in_dst_from,
                          "nights_in_dst_to": self.nights_in_dst_to,
                          "max_stopovers": self.max_stopovers,
                          "curr": self.curr,
                          "price_to": f"{price_to}",
                          "one_for_city": self.one_for_city}
        response = requests.get(url=url, params=request_params, headers=self.api_headers)
        raw_data = response.json()
        # pprint(raw_data)

        if raw_data['_results'] == 1:
            data = raw_data['data'][0]
            route = data["route"]
            if len(route) == 2:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=route[0]["cityFrom"],
                    origin_airport=route[0]["flyFrom"],
                    destination_city=route[0]["cityTo"],
                    destination_airport=route[0]["flyTo"],
                    out_date=route[0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0]
                )
            elif len(route) > 2:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=route[0]["cityFrom"],
                    origin_airport=route[0]["flyFrom"],
                    destination_city=route[1]["cityTo"],
                    destination_airport=route[1]["flyTo"],
                    out_date=route[2]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=route[0]["cityTo"]
                )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
        else:
            print(f"No flights found for {to_iata_code}.")
            return None



# !L5!3@32k2FEGxg