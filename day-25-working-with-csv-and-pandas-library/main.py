import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()

temp_list = data["temp"].to_list()

# getting average temperature from the data
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# print(data["temp"].mean())
#
# # getting the highest temp in the data
# print(data["temp"].max())
#
# # get the data in the column
# print(data["condition"])
# print(data.condition)
# print(data.temp.max())


# get the data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday)
celsius_temp = monday.temp[0]
print(celsius_temp)
fahrenheit_temp = (celsius_temp * (9 / 5)) + 32
print(fahrenheit_temp)

# create data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 87, 91]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")