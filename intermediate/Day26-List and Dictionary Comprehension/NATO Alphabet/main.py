import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(data)

# Create a dict in this format. {'A': 'Alfa', 'B': 'Bravo' , ...}

# letter_dict = {}
# for (index, row) in data.iterrows():
#     letter_dict[row['letter']] = row['code']
#
# print(letter_dict)

# or
letter_dict = {row['letter']: row['code'] for (index, row) in data.iterrows()}
# print(letter_dict)

# Create a list of phonetic code words from a word that user input
user_input = input("Enter a word: ")

# phonetic_list = []
# for letter in list(user_input.upper()):  # split a word into individual letters
#     if letter in letter_dict.keys():
#         phonetic_list.append(letter_dict[letter])
#
# print(phonetic_list)

# or
phonetic_list = [letter_dict[letter] for letter in list(user_input.upper()) if letter in letter_dict.keys()]
print(phonetic_list)