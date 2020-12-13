import pandas

letters_list = pandas.read_csv("nato_phonetic_alphabet.csv")


def name_spelling():
    word = input("Please, enter a word: ").upper()
    phonetic_dict = {v.letter: v.code for (k, v) in letters_list.iterrows()}
    output_list = {letter: phonetic_dict[letter] for (letter) in word}
    print(output_list)


name_spelling()
