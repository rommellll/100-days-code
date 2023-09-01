import smtplib
import datetime as dt
import random
import json

with open("../../secret.json") as secret:
    credential = json.load(secret)
    email = credential['email']
    password = credential['password']


def send_mail(recipient, subject, body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=recipient,
                            msg=f"Subject: {subject}.\n\n{body}"
                            )


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    send_mail(recipient=email, subject="Monday Motivations", body=quote)


