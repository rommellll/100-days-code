# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     next(data)
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("../weather_data.csv")
print(data["temp"])