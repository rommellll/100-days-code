import json
import time

import requests
import smtplib
from datetime import datetime

# gmail credentials
with open("../../secret.json") as secret:
    credentials = json.load(secret)
    email = credentials["email"]
    password = credentials["password"]

# LAT = 14.869614
# LONG = 120.801482
LAT = 31
LONG = -50


def is_iss_above():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_position = (iss_latitude, iss_longitude)
    if ((LAT - 5) <= iss_latitude <= (LAT + 5)) and ((LONG - 5) <= iss_longitude <= (LONG + 5)):
        return True
    return False

def is_night_time():
    parameters = {
        "lat": LAT,
        "long": LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True
    return False


def send_mail(recipient, body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(to_addrs=recipient,
                            from_addr=email,
                            msg=f"Subject: Look up!\n\n {body}")


while True:
    time.sleep(60)
    if is_night_time() and is_iss_above():
        send_mail(recipient="rommel52595@gmail.com", body=f"Look up in the sky, the current position of iss above your location.")