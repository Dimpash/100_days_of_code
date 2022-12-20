import smtplib
import datetime as dt
import random


MY_EMAIL = "mitya.p.76.exp@gmail.com"
MY_PASSWORD = "exp,123698745"
destination_email = "mitya_76@mail.ru"

now = dt.datetime.now()
now_weekday = now.weekday()

with open("quotes.txt", "r") as f:
    quotes = f.readlines()


quote = random.choice(quotes)
message = f"Subject:Motivation quote\n\n{quote}"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=destination_email, msg=message)

