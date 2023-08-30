import pandas as pd


# turn csv to a dictionary
nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def converter():
    # convert input word to a nato alphabet
    word = list(input("Enter a word: ").upper())
    try:
        converted_word = [nato_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        converter()
    else:
        print(converted_word)


converter()