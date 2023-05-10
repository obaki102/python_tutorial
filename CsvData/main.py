# import csv

# with open("CsvData\data\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temparatures = []
#     for row in data:
#         temparatures.appendrow[1]
        
import pandas

data = pandas.read_csv("CsvData\data\weather_data.csv")
print(data)
data_dictionary =  data.to_dict()
print(data_dictionary)
temp_list = data["temp"].tolist()
print(temp_list)
print(f"max temp: {data.temp.max()}")

# get row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# creating data frame from in memory data
data_dict = {
    "students": ["Josh","Josh 2","Josh 3"],
    "scores": [1,2,3]
}
data_frame  = pandas.DataFrame(data_dict)
data_frame.to_csv("new_data.csv")

