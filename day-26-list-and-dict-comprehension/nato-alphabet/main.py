import pandas as pd

# turn csv to a dictionary
nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# convert input word to a nato alphabet
word = list(input("Enter a word: ").upper())
converted_word = [nato_alphabet_dict[letter] for letter in word]
print(converted_word)