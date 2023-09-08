import requests
import json
from datetime import datetime

with open("../secret.json") as secrets:
    credentials = json.load(secrets)


USERNAME = credentials["pixela_username"]
TOKEN = credentials["pixela_api_key"]
pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "romosa-graph-1"
graph_config = {
    "id": "romosa-graph-1",
    "name": "Walking",
    "unit": "Steps",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.today()
walking_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
graph_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5449"
}

# response = requests.post(url=walking_graph_endpoint, json=graph_data, headers=headers)
# print(response.text)
print(graph_data)