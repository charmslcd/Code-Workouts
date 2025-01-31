# with open("weather_data.csv", mode="r") as file:
#     data = [line.strip() for line in file]
#
# print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
#
# data_dic = data.to_dict()
# print(data_dic)
#
# data_list = data["temp"].to_list()

# #manual compute for ave
# sum_var = 0
# for data in data_list:
#     sum_var += data
#
# ave = sum_var / len(data_list)
# print(ave)
#
# #compute for ave using built in python methods
# ave = sum(data_list)/len(data_list)
# print(ave)

#compute for ave using pandas lib

# ave = data["temp"].mean()
# print(ave)
#
# max = data["temp"].max()
# print(max)

# print(data[data.day == "Monday"])

# print(data[data.temp == max])
#
# monday = data[data.day == "Monday"].temp
# convert = monday * (9/5) + 32
# print(convert)

#Create dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")