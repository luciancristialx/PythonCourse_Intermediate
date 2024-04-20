import requests
import os
from twilio.rest import Client

ACCOUNT_SID = ""
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

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
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages\
        .create(body = "It's going to rain today. Remember to bring an umbrella!", from_ = '+12513125281',
        to = os.environ.get('PHONE_NR'))
    print(message.status)