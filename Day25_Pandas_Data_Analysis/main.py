import pandas as pd

data_frame = pd.read_csv("squirrel_count.csv")
# print(data_frame)

#Get all squirrels with Grey color
grey_squirrels_count = len(data_frame[data_frame["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data_frame[data_frame["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data_frame[data_frame["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(cinnamon_squirrels_count)
# print(black_squirrels_count)

data_dict ={
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("count.csv")