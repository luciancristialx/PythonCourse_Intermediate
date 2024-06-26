
import os
import requests
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.token = os.environ["SHEETY_TOKEN"]
        self.endpoint = os.environ["SHEETY_ENDPOINT"]
        self.destination_data={}

    def get_destination_data(self):
        sheety_header = {
            "Authorization": self.token
        }
        response = requests.get(url=self.endpoint,headers = sheety_header)
        data = response.json()
        if 'errors' in data:
            test_dict = {
                "destinations":[
                    { "id": 2,
                      "city": "Rome",
                      "iataCode": "ROM",
                      "lowestPrice": "400"
                    },
                    { "id": 3,
                      "city": "Paris",
                      "iataCode": "PAR",
                      "lowestPrice": "400"
                    },
                    { "id": 4,
                      "city": "London",
                      "iataCode": "LON",
                      "lowestPrice": "400"
                    },
                    { "id": 5,
                      "city": "Gatwick",
                      "iataCode": "LGW",
                      "lowestPrice": "400"
                    }
                ]
            }
            self.destination_data=test_dict["destinations"]
        else:
            self.destination_data=data["destinations"]
        return self.destination_data

    def update_destination_codes(self):
        sheety_header = {
            "Authorization": self.token
        }
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response=requests.put(url = f"{self.endpoint}/{city['id']}",json = new_data,headers = sheety_header)
            print(response)
