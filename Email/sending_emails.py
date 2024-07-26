import smtplib
import datetime as dt
import random


MY_EMAIL = "m*@esbit.vitebsk.energo.net"
MY_PASSWORD = "*"
destination_email = "m*@mail.ru"

now = dt.datetime.now()
now_weekday = now.weekday()

with open("quotes.txt", "r") as f:
    quotes = f.readlines()

if now_weekday == 3:
    quote = random.choice(quotes)
    message = f"Subject:Motivation quote\n\n{quote}"
    with smtplib.SMTP("mail.esbit.vitebsk.energo.net") as connection:
        # connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=destination_email, msg=message)

