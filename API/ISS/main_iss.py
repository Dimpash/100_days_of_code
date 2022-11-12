import requests
from datetime import datetime
import math
import smtplib
import time
import auth_data

MY_LAT = 55.184807
MY_LONG = 30.201622
DELTA = 5.0

MY_EMAIL = auth_data.WORK_EMAIL
MY_PASSWORD = auth_data.WORK_PASSWORD
destination_email = auth_data.destination_email

proxies = {
        'http': auth_data.http_proxy,
        'https': auth_data.https_proxy,
    }

response = requests.get(url="http://api.open-notify.org/iss-now.json", proxies=proxies)
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", proxies=proxies, params=parameters)
response.raise_for_status()
data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
sunrise = datetime.strptime(data["results"]["sunrise"].split("T")[1].split("+")[0], '%H:%M:%S').time()
sunset = datetime.strptime(data["results"]["sunset"].split("T")[1].split("+")[0], '%H:%M:%S').time()
# datetime.strptime()

time_now = datetime.now().time()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def sending_email():
    message = "Subject:ISS infomation\n\nYou can see ISS in the sky right now."
    with smtplib.SMTP("mail.esbit.vitebsk.energo.net") as connection:
        # connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=destination_email, msg=message)

def check_iss():
    # print(f"iss_latitude={iss_latitude}, iss_longitude={iss_longitude}")
    # print(f"sunrise={sunrise}, sunset={sunset}")
    # print(f"time_now={time_now}")
    if (math.fabs(MY_LAT - iss_latitude) <= DELTA) and (math.fabs(MY_LONG - iss_longitude) <= DELTA) and (
            (time_now > sunset) or (time_now < sunrise)):
        print("You can see ISS in the sky right now. Look up.")
        sending_email()
        return True
    else:
        print("You need to wait")
        return False

exit_key = False

while not exit_key:
    time.sleep(60)
    exit_key = check_iss()


