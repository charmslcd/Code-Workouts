# output count of all colors from Primary fur column

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(gray_squirrels)
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(red_squirrels)
black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels)
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data_frame = pd.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")
