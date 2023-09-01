import requests


def get_questions():
    opentdb_api_url = "https://opentdb.com/api.php"
    parameters = {
        "amount": 10,
        "type": "boolean"
    }

    response = requests.get(url=opentdb_api_url, params=parameters)
    data = response.json()
    return data


questions = get_questions()
question_data = questions["results"]