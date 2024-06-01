# List comprehension

# ex-1
# num_list = [1, 2, 3, 4, 5, 6]

# new_list = []
# for num in num_list:
#     new_list.append(num*num)
#
# print(new_list)

# or
# new_list = [num * num for num in num_list]
# print(new_list)

# ex-2
# even_list = []
# for num in num_list:
#     if num % 2 == 0:
#         even_list.append(num)
#
# print(even_list)


# or
# even_list = [num for num in num_list if num % 2 == 0]
# print(even_list)

# ex-3
# doubled_list = [n * 2 for n in range(1, 5)]
# print(doubled_list)

# ex-4
# names = ['Alex', 'Sara', 'Bob', 'Michale', 'David', 'Bruno']
# names_less_than_five = [name for name in names if len(name) < 5]
# print(names_less_than_five)  # ['Alex', 'Sara', 'Bob']
#
# uppercase_names = [name.upper() for name in names if len(name) >= 5]
# print(uppercase_names)  # ['MICHALE', 'DAVID', 'BRUNO']

# ex-5 : get a letter, number pair
# new_pair = []
# for letter in 'abcd':
#     for num in range(4):
#         new_pair.append((letter,num))
#
# print(new_pair)

# or
# new_pair = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(new_pair)


# -------------------------------------------------------------------


# Dictionary Comprehension

# eg-1
names = ['Alex', 'Sara', 'Bob', 'Michale', 'David', 'Bruno']
ages = [29, 30, 16, 27, 19, 21]

# person_dict = {}
# for name, age in zip(names, ages):
#     person_dict[name] = age
#
# print(person_dict)  # {'Alex': 29, 'Sara': 30, 'Bob': 16, 'Michale': 27, 'David': 19, 'Bruno': 21}


# or
# person_dict = {name: age for name, age in zip(names, ages)}
# print(person_dict)   # {'Alex': 29, 'Sara': 30, 'Bob': 16, 'Michale': 27, 'David': 19, 'Bruno': 21}
#
# # with condition
# dict_without_alex = {name: age for name, age in zip(names, ages) if name != 'Alex'}
# print(dict_without_alex)  # {'Sara': 30, 'Bob': 16, 'Michale': 27, 'David': 19, 'Bruno': 21}
#
# # dictionary with ages > 21
# greater_than = {name: age for (name, age) in person_dict.items() if age > 21}
# print(greater_than)


# eg-2 : You are going to use Dictionary Comprehension to create a dictionary called result
# that takes each word in the given sentence and calculates the number of letters in each word.

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list_of_words = sentence.split(" ")
# # print(list_of_words)
#
# result = {word: len(word) for word in list_of_words}
# print(result)


# eg-3 : create a dictionary called weather_f that takes each temperature in degrees Celsius
# and converts it into degrees Fahrenheit.

# To convert temp_c into temp_f use this formula:
# (temp_c * 9/5) + 32 = temp_f

# The eval() function will help us convert the string input into a Python dictionary,
# provided that the inputs are already formatted with the correct syntax.


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}


def temp_f(val):
    return (val * 9 / 5) + 32


weather_f = {day: temp_f(val) for (day, val) in weather_c.items()}
print(weather_f)

