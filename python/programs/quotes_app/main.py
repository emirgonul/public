from tkinter import *
import random
import requests

#set background color
BACKGROUND_COLOR = "#B1DDC6"

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    #check for api response status
    response.raise_for_status()
    #get json data from response
    data = response.json()
    #get quote from data
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

#shuffle button image
def get_images():
    n = random.randint(1,2)
    return f"images/kanye{n}.png"


window = Tk()
window.title("kanye api data")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=300, height=414)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="My life is dope and I do dope shit.", width=250, font=("Arial", 28, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=get_images())
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()