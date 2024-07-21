import smtplib
import os

MY_SMTP = "smtp.gmail.com"
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')
DESTINATION_EMAILS = ["mitya_76@mail.ru"]

# print(MY_EMAIL)
# print(MY_PASSWORD)


def email_sending(destination_email, subject, email_text):
    message = f"Subject:{subject}\n\n{email_text}"
    with smtplib.SMTP(MY_SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=destination_email, msg=message)


def send_by_dest_list(subject, email_text, destination_emails=DESTINATION_EMAILS):
    for dest_email in destination_emails:
        email_sending(dest_email, subject, email_text)


