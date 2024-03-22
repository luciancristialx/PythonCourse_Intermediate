import pandas as pd

data = pd.read_csv("./nato_phonetic_alphabet.csv")

nato_phonetic_alphabet = {row.letter:row.code for (index,row) in data.iterrows()}
print(nato_phonetic_alphabet)

def generate_phonetic():
    name = input("Enter a word:")
    letters_name = [letter.upper() for letter in name]
    try:
        phonetic_word = [nato_phonetic_alphabet[letter] for letter in letters_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_word)

generate_phonetic()