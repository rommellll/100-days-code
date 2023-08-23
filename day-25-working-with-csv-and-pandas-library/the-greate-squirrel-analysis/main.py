import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_color = data["Primary Fur Color"].dropna().unique().tolist()
squirrel_color_count = []
for color in squirrel_color:
    color_count = data[data["Primary Fur Color"] == color]
    squirrel_color_count.append(len(color_count))

data_dict = {
    "Color": squirrel_color,
    "Count": squirrel_color_count
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")