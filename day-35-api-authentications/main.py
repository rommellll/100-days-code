import requests
import os
from twilio.rest import Client


api_key = os.environ.get("OWM_API_KEY")
TWILIO_NUM = os.environ.get("TWILIO_NUM")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
MY_NUM = os.environ.get("MY_NUM")
OWM_API_URL = "https://api.openweathermap.org/data/3.0/onecall"

params = {
    "lat": 25.872380,
    "lon": 111.758324,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
client = Client(account_sid, auth_token)


response = requests.get(OWM_API_URL, params=params)
response.raise_for_status()

weather_data = response.json()
hourly_weather = weather_data["hourly"]
condition_code = [hourly_weather[key]["weather"][0]["id"] for key in range(12)]

if min(condition_code) < 700:
    print("Bring an umbrella, uulan kase.")
    message = client.messages \
        .create(
        from_=TWILIO_NUM,
        body='Bring an umbrella, uulan kase. ☂️',
        to=MY_NUM
    )
    print(message.status)