import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
#dict to save selected french:english word
current_word = {}
to_learn = {}

#data frame
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError: #if words_to_learn.csv dont exist, use the original french_words file
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records") #create list of dicts
else:
#create list of dicts
    to_learn = data.to_dict(orient="records")


def word_shuffle():
    global current_word, flip_timer
    #invalidate timer when button is pressed
    window.after_cancel(flip_timer)
    #select a random word
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word['French'], fill="black")
    #update card background image to card_front_img
    canvas.itemconfig(card_background, image=card_front_img)
    #delay of 3s for word card to flip
    flip_timer = window.after(3000, func=flip_word)

def flip_word():
    #change word from french to english
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word['English'], fill="white") 
    #update card background image to card_back_img
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    #remove current word
    to_learn.remove(current_word)
    #keep a record of unknown words
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    #shuffle again    
    word_shuffle()


window = Tk()
window.title('Flash')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#delay of 3s for word card to flip
flip_timer = window.after(3000, func=flip_word)

#canvas object & create custom canvas
canvas = Canvas(width=800, height=526)
#card images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
#card background
card_background = canvas.create_image(400, 263, image=card_front_img)
#card data
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#setup buttons
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=word_shuffle)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

#call word shuffle for initial setup
word_shuffle()

window.mainloop()