import requests
import datetime as dt
import json

with open("../secret.json") as secrets:
    credentials = json.load(secrets)


today = dt.datetime.today()
today_date = today.strftime("%Y-%m-%d")
today_time = today.time().strftime("%H:%M:%S")

nutritionix_api_key = credentials["nutritionix_api_key"]
nutritionix_app_id = credentials["nutritionix_app_id"]
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api_key
}
exercise_data = {
    "query": input("What exercise you did?"),
    "gender": "male",
    "weight_kg": 62,
    "height_cm": 164,
    "age": 28
}


response = requests.post(url=nutritionix_endpoint, headers=headers, json=exercise_data)
data = response.json()
exercises = data["exercises"]

sheety_token = credentials["sheety_api_key"]
sheety_endpoint = "https://api.sheety.co/8320fbbe957c3da8d06735b0f8f67862/workouts/workouts"

sheety_header = {
    "Authorization": f"Bearer {sheety_token}"
}

# for exercise in exercises:
#     sheety_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": today_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
#     sheet_response = requests.post(url=sheety_endpoint, headers=sheety_header, json=sheety_inputs)

response = requests.get(url=sheety_endpoint, headers=sheety_header)
data = response.json()
workouts = list(data["workouts"])
print(workouts[0])