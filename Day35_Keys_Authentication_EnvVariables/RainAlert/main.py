import requests
import os

API_KEY = os.environ.get('OWM_API_KEY')
API_URL = "https://api.openweathermap.org/data/2.5/forecast"
LAT = "44.426765"
LON = "26.102537"

parameters = {
    "lat":LAT,
    "lon":LON,
    "cnt":4,
    "appid":"bc6770ef025212d141f0981eb42ba919"
}

response = requests.get(API_URL, params = parameters)
response.raise_for_status()
data = response.json()

weather_data = data["list"]

will_rain = False
for hour_data in weather_data:
    li_weather = hour_data["weather"]
    for weather in li_weather:
        if int(weather["id"]) < 700:
            will_rain = True

if will_rain:
    print("Bring an umbrella.")
else:
    print("All good.")



# print(data)