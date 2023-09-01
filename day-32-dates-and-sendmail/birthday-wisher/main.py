import datetime as dt
import random, os, json, smtplib
import pandas as pd

with open("../../secret.json") as secret:
    credentials = json.load(secret)
    email = credentials["email"]
    password = credentials["password"]
now = dt.datetime.now()
month_day = now.day
month = now.month
today = (month, month_day)
templates = (os.listdir("letter_templates"))
letter_name_placeholder = "[NAME]"


def send_mail(recipient_email, body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=recipient_email,
                            msg=f"Subject: Happy Birthday!\n\n{body}")


data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    person_birthday = birthdays_dict[today]
    person_name = person_birthday["name"]
    person_email = person_birthday["email"]
    template = random.choice(templates)
    with open(f"letter_templates/{template}") as file:
        letter = file.read()
        updated_letter = letter.replace(letter_name_placeholder, person_name)
    send_mail(recipient_email=person_email, body=updated_letter)
