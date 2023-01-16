#from the csv file, get fur colors of squirrels by number and write into new csv table
import pandas

#open file with panda
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#get hold of colors & the number of colors from the data
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

#create dict
data_dict = {
    "fur colors": ["gray", "red", "black"],
    "count": [gray_squirrel, red_squirrel, black_squirrel]
}

#initialize dataframe
df = pandas.DataFrame(data_dict)
#write to file
df.to_csv("squirrel_color_count.csv")
