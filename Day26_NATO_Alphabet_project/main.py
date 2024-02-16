import pandas as pd

data = pd.read_csv("./nato_phonetic_alphabet.csv")

nato_phonetic_alphabet = {row.letter:row.code for (index,row) in data.iterrows()}

name = input("Enter a word:")
letters_name = [letter.upper() for letter in name]

phonetic_word = [nato_phonetic_alphabet[letter] for letter in letters_name]
print(phonetic_word)