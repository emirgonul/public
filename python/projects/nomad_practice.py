#note taking script for medical setting where a doctor can take notes and have them in a list at the end of the diagnosis
#write a function that takes in text as a string & prints out an sorted list


#prompt the doctor to enter a number to start off the list
note_number = int(input("Enter a number to start a list: "))

def patient_notes(note_number):
    #list to capture notes
    visit_info = []
    #flag for while loop to capture multiple enteries
    number_next = True 
    while number_next:
        #dict to collect number:notes
        notes = {}
        #capture entered note
        notes[note_number] = input("Enter a note: ")
        #doctor's next note, else stop loop and print the info
        should_continue = input("Please enter the next action('y' or 'n'): ").lower
        visit_info.append(notes)
        if should_continue == "y":
            number_next = True
            note_number += 1
        else:
            number_next = False

    #format entered data to print
    print(f"Patient presents today with several issues.")
    #loop through list of dicts to seperate and format key:value data for print
    for i in visit_info:
        for key in i.keys():
            number = key
        for value in i.values():
            #capitalize entered value
            note = value.capitalize()
        #print out list of notes
        print(f"{number}. {note} ")


patient_notes(note_number)
