import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""

GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 180
AGE = 29

Bearer_Auth = "Bearer Token"

nutritionix_endpoint = "https://trackapi.nutritionix.com//v2/natural/exercise"

sheety_endpoint = "https://api.sheety.co/0aea9bf6601289f32cc556a03c373aac/workouts/workouts"

query = input("Tell me what exercise you did: ")

nutritionix_exercise_nlp_headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}

nutritionix_exercise_nlp_body ={
    "query":query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutritionix_response =requests.post(url = nutritionix_endpoint,json = nutritionix_exercise_nlp_body,headers =
nutritionix_exercise_nlp_headers)
nutritionix_response.raise_for_status()

nutritionix_data = nutritionix_response.json()["exercises"]

print(nutritionix_data)

for exercise in nutritionix_data:
    sheety_header = {
        "Authorization": Bearer_Auth
    }

    sheety_body = {
        "workout":{
            "date":datetime.now().strftime("%d/%m/%Y"),
            "time":datetime.now().strftime("%X"),
            "exercise":exercise["name"].capitalize(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url = sheety_endpoint,json = sheety_body, headers = sheety_header)
    sheety_response.raise_for_status()
    print(sheety_response.text)