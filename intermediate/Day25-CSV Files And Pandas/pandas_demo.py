import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# DataFrame conversion:
# data_dict = data.to_dict()
# print(data_dict)

# Series conversion
# series_to_list = data["temp"].to_list()
# print(series_to_list)

# get avg temp
# avg_temp = data['temp'].mean()
# print(round(avg_temp, 2))

# sum_of_temp = 0
# for temp in series_to_list:
#     sum_of_temp += temp
# avg_temp = sum_of_temp/len(series_to_list)

# print(f"Average temp is: {avg_temp}")

# get max temp
# max_temp = data['temp'].max()
# print(max_temp)

# get specific row
#  with max temp
# max_temp_row = data[data['temp'] == max_temp]
# print(max_temp_row)

# get monday's row temp and change it into Fahrenheit

# monday_row = data[data['day'] == 'Monday']
# monday_temp_c = monday_row.temp[0]
# temp_in_f = (monday_temp_c * (9/5)) + 32
# print(temp_in_f)


# Create a dataframe from stretch
dict_data = {
    "Name": ["Susil", "Aryan", "Vikash"],
    "Age": [21, 22, 23],
}

student_data = pd.DataFrame(dict_data)
# print(student_data)

# convert to csv file
student_data.to_csv("student.csv")