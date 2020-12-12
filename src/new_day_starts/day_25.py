import csv
import pandas

# from pandas import DataFrame


# with open("../weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = [int(i[1]) for i in data if i[1] != "temp"]
# print(*temperatures)


# data = pandas.read_csv("../weather_data.csv")
# print(data["temp"])
# lst = data["temp"]
# temp_list = data["temp"].to_list()
# average = round(sum(temp_list) / len(temp_list), 2)
# print(average)
# maximum = lst.max()
# print(maximum)

# print(data[data.temp == maximum])

# monday = data[data.day == "Monday"]

# mon_temp = (monday.temp * 9/5) + 32
# print(mon_temp)


# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(colors)
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_count = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, cinnamon, black]
}

data_squirrel = pandas.DataFrame(data_count)
data_squirrel.to_csv("squirrel_count.csv")
