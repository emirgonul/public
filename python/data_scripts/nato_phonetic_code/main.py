#program to code words to phonetic alphabet
import pandas

#create a dictionary from csv data
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = data.to_dict()
#isolate row and build letter:code key:value pair
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
#pass each letter from input to the dict and print the value letter:code_word
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
