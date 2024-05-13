
# Using csv module
import csv


# Read from CSV file
with open("./weather_data.csv") as csv_file:
    # data = file.readlines()
    # print(data)
    # temperatures = []
    csv_reader = csv.reader(csv_file) # read a csv file

    # skip the first list
    # next(csv_file)

    # for data in csv_reader:
    #     # print(data)
    #     if data[1] != "temp":
    #         temperatures.append(int(data[1]))
    # print(temperatures)

    # write in a csv file
    with open("new_data.csv", mode="w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="/")

        for line in csv_reader:
            csv_writer.writerow(line)


