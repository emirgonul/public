#1. convert the guess to Title case
#2. check if the guess is among the 50 states
#3. write correct guesses onto the map
#4. use a loop to allow the user to keep guessing
#5. record the correct guesses in a list
#6. keep track of the score
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
#add image to screen
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
#convert data to list
all_states = data.state.to_list()
#keep track of guesses
guessed_states = []

#prompt until 50 states all are guessed
while len(guessed_states) < 50:
  answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                  prompt="What's another state's name?").title()
  #exit to kill game 
  if answer_state == "Exit":
    #if a state is not in guessed_states, it's a missed state
    missing_states = [state for state in all_states if state not in guessed_states]
    #construct data frame of missing states
    new_data = pandas.DataFrame(missing_states)
    #write to file states that were missed by the user
    new_data.to_csv("states_to_learn.csv")

    break
  #if the answer is one of the states in the csv
  #if correct, write name to the x, y coordinates
  if answer_state in all_states:
    #add to list when guess state is correct
    guessed_states.append(answer_state)
    #construct turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    #retrieve the row where answer is equal to the list
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)