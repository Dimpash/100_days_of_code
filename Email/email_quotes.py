import smtplib
import datetime as dt
import random
import os


MY_SMTP = "smtp.gmail.com"
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')
destination_emails = ["m*@mail.ru", "e*@gmail.com", "s*@gmail.com"]

now = dt.datetime.now()
now_weekday = now.weekday()

with open("quotes.txt", "r") as f:
    quotes = f.readlines()


def quote_sending(destination_email):
    quote = random.choice(quotes)
    message = f"Subject:Motivation quote\n\n{quote}"
    with smtplib.SMTP(MY_SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=destination_email, msg=message)


for dest_email in destination_emails:
    quote_sending(dest_email)


# now = dt.datetime.now()
# now_weekday = now.weekday()
#
# with open("quotes.txt", "r") as f:
#     quotes = f.readlines()
#
#
# quote = random.choice(quotes)
# message = f"Subject:Motivation quote\n\n{quote}"
# with smtplib.SMTP(MY_SMTP) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL, to_addrs=destination_email, msg=message)

