#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime as dt
from pprint import pprint
import smtplib
import os

from data_manager import DataManager
from flight_search import FlightSearch
from users_manager import UsersManager

sheet_worker = DataManager()
flight_searcher = FlightSearch()
users_worker = UsersManager()

smtp_user = os.environ.get('MY_EMAIL')
smtp_password = os.environ.get('MY_PASSWORD')

def work_with_flights():
    # Update IATA codes
    sheet_data = sheet_worker.get_data()
    # pprint(sheet_data)
    users_data = users_worker.get_data()

    for item in sheet_data:
        if item['iataCode'] == '':
            iata_code = flight_searcher.get_iata_code(city_name=item['city'])
            # print(iata_code)
            sheet_data['iataCode'] = iata_code
            sheet_worker.save_iata_code(id=item['id'], iata_code=iata_code)

    for item in sheet_data:
        flight = flight_searcher.get_flight_info(to_iata_code=item['iataCode'], price_to=item['lowestPrice'])
        if flight is not None:
            for user in users_data:
                destination_email = user['email']
                message = f"Low price alert! Only {flight.price}GBP to fly from {flight.origin_city}-" \
                          f"{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from " \
                          f"{flight.out_date} to {flight.return_date}."
                if flight.stop_overs > 0:
                    message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=smtp_user, password=smtp_password)
                    connection.sendmail(from_addr=os.environ.get('MY_EMAIL'), to_addrs=destination_email, msg=message)


if input("Input operation type: work_with_flights - 1, work_with_users - 2: ") == '1':
    work_with_flights()
else:
    while users_worker.add_user() == 'y':
        pass