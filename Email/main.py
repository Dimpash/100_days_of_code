##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import datetime as dt
import smtplib
from random import randint

MY_EMAIL = "main-it@esbit.vitebsk.energo.net"
MY_PASSWORD = "20011954"

# Angela version
#Bad thing: it works only for one person in file
# today = (dt.datetime.now().month, dt.datetime.now().day)
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(row["month"], row["day"]): row for index, row in data.iterrows()}


# My version
birthdays = pandas.read_csv("birthdays.csv")
now_month = dt.datetime.now().month
now_day = dt.datetime.now().day

for index, row in birthdays.iterrows():
    if row.day == now_day and row.month == now_month:
        file_name = f"letter_templates\letter_{randint(1,3)}.txt"
        with open(file_name, "r") as file:
            message = f"Subject:Happy birthday to you!\n\n{file.read().replace('[NAME]', row['name'])}"
        with smtplib.SMTP("mail.esbit.vitebsk.energo.net") as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row["email"], msg=message)


#


