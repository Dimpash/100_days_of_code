import os

import requests
import datetime as dt

GENDER = "male"
WEIGHT = 90.2
HEIGHT = 179
AGE = 76

nutrionix_endpoint = "https://trackapi.nutritionix.com/v2/natural"
X_APP_ID = os.environ.get('X_APP_ID')
X_APP_KEY = os.environ.get('X_APP_KEY')
x_remote_user_id = "0"
nutrionix_headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": X_APP_KEY,
    "x-remote-user-id": x_remote_user_id
}

sheety_endpoint = "https://api.sheety.co/d57a1b9ad4ed64e22745313802ffb155/dzmitryWorkouts/workouts"
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
sheety_headers = {"Authorization": "Bearer " + SHEETY_TOKEN}

#  Exercise work

def get_exercise_info():
    exercise_endpoint = f"{nutrionix_endpoint}/exercise"

    exercise_text = input("Please describe what exercises you did: ")

    request_config = {
        "query": exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE
    }

    response = requests.post(url=exercise_endpoint, json=request_config, headers=nutrionix_headers)
    result = response.json()
    # print(result)
    return result

# Sheety work
response = requests.get(url=sheety_endpoint, headers=sheety_headers)
# print(response.text)


def save_workout_info():
    exercises = get_exercise_info()['exercises']
    saving_date = dt.datetime.now()
    date = saving_date.strftime('%d/%m/%Y')
    time = saving_date.strftime('%X')

    for exercise in exercises:
        request_config = {'workout': {"date": date,
                                      "time": time,
                                      "exercise": exercise["name"].title(),
                                      "duration": exercise["duration_min"],
                                      "calories": exercise["nf_calories"],
                                      "id": 2}
                          }
        response = requests.post(url=sheety_endpoint, json=request_config, headers=sheety_headers)
        print(response.text)


save_workout_info()