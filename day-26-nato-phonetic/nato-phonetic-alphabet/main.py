import pandas as pd
from math import log

nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        result_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result_list)


generate_phonetic()
# result_list = [catch(log, letter) for letter in user_input]



