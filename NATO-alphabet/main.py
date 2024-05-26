import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:

    try:
        name = input("Enter your name: ").upper()
        phonetic_code = [phonetic_dict[letter] for letter in name]
    except KeyError:
        print("Please enter letters in alphabet only.")

    else:
        print(phonetic_code)
