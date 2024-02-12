import csv

import pandas
import pandas as pd

# with open("./Input/weather_data.csv") as weather_data_file:
#     data = weather_data_file.readlines()
#     print(data)

# print("\nGet numeric values from temp column:\n")
# with open("./Input/weather_data.csv") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pd.read_csv("./Input/weather_data.csv")
# print(type(data))
# print(data["temp"])
# print(type(data["temp"]))

# data_dict = data.to_dict()
#print(data_dict)

# temp_list = data["temp"].tolist()
#print(temp_list)

# avg = data["temp"].mean
#
# max_temp = data["temp"].max()
# print(f"Max temp: {max_temp}\n")

#Get data in columns
# print(data["condition"])
# print("\n")
# print(data.condition)

#Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
#print(monday.condition)
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)


#Create DF

data_dict = {
    "students":["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_DF = pandas.DataFrame(data_dict)
data_DF.to_csv("new_data.csv")