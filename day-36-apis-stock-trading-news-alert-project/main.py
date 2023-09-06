import requests
import pytz
import holidays
from twilio.rest import Client
from datetime import datetime, timedelta
import json

with open("../secret.json") as secrets:
    credentials = json.load(secrets)

us_east_tz = pytz.timezone("US/Eastern")
now = datetime.now(us_east_tz).date()


def business_day(date):
    while date in holidays.US() or date.weekday() > 4:
        date = date - timedelta(1)
    return date


def send_sms(body):
    twilio_num = credentials["twilio_num"]
    account_sid = credentials["twilio_account_sid"]
    auth_token = credentials["twilio_account_token"]
    my_num = credentials["my_num"]

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        from_=twilio_num,
        body=body,
        to=my_num
    )
    print(message.status)


def get_stock_info():
    stock_code = "TSLA"
    date_yesterday = business_day(now - timedelta(1))
    date_previous_day = business_day(date_yesterday - timedelta(1))
    stock_api_key = credentials["stock_trading_view_api_key"]
    stock_api_url = "https://www.alphavantage.co/query"
    stock_api_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_code,
        "apikey": stock_api_key
    }

    stock_api_response = requests.get(stock_api_url, params=stock_api_params)
    stock_api_response.raise_for_status()
    data = stock_api_response.json()
    daily_data = data['Time Series (Daily)']
    closing_yesterday = float(daily_data[str(date_yesterday)]["4. close"])
    closing_previous_day = float(daily_data[str(date_previous_day)]["4. close"])
    percentage = round(100 * ((closing_yesterday - closing_previous_day) / closing_previous_day), 2)
    if percentage > 0:
        stock_status = f"📈{stock_code} is up over {percentage}%"
    else:
        stock_status = f"📉{stock_code} is down over {-1 * percentage}%"
    return stock_status


def get_headline():
    news_api_key = credentials["newsorg_api_key"]
    news_api_url = "https://newsapi.org/v2/top-headlines"

    news_api_params = {
        "q": "Tesla",
        "apiKey": news_api_key
    }

    news_api_response = requests.get(news_api_url, params=news_api_params)
    news_api_response.raise_for_status()
    news_data = news_api_response.json()
    news_articles = news_data["articles"]
    headline_title = news_articles[0]["title"]
    return headline_title


message = f"{get_stock_info()}\n{get_headline()}"
send_sms(body=message)
