#create unique letters from template and list of names text file 

NAMES = "./Input/Names/invited_names.txt"
LETTER = "./Input/Letters/starting_letter.txt"
OUTPUT = "./Output/ReadyToSend/"
PLACEHOLDER = "[name]"


with open(NAMES, mode="r") as names_file:
    #readlines() convert each line is an item in a list object
    names = names_file.readlines()

with open(LETTER, mode="r") as letter_file:
    #set letter contents to a variable
    letter_contents = letter_file.read()
    #get names from names list, replace [names] placeholder with name
    for name in names:
        #eliminate extra lines
        stripped_name = name.strip()
        #replace placeholder with individual names to create a new letter
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) 
        #write new letter as a text file
        with open(f"{OUTPUT}letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)