from csv_operation import csv_reader


data2020 = csv_reader("2020file.csv", "data")
print(data2020[0], "#" * 10, data2020[1], "#" * 10, " \n", data2020[2])

print("-*-" * 10)
data2019 = csv_reader("2019file.csv", "data")
print(data2019[0], "#" * 10, data2019[1], "#" * 10, " \n", data2019[2])

print("1. Heat comparison")
print(len(data2020), " VS ", len(data2019))
