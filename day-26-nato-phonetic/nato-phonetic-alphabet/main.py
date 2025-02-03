#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd

with open("nato_phonetic_alphabet.csv") as file:
    nato = pd.read_csv(file)

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
# print(type(nato_dict))


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ")
input_list = [letter.upper() for letter in user_input]

# print(nato_dict)
# print(input_list)

result_list = [nato_dict[letter] for letter in input_list]
print(result_list)



