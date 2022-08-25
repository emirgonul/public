from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.score = 0
    #change color before writing text
    self.color("white")
    self.penup()
    #move text & hide initial turtle 
    self.goto(0, 280)
    self.hideturtle()
    #update the scoreboard
    self.update_scoreboard()
    
  #display score
  def update_scoreboard(self):
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
  #increase score and write it on the board
  def increase_score(self):
    self.score += 1
    #wipe previous scoreboard and write new
    self.clear()
    self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

  def game_over(self):
    #write game over at the center
    self.goto(0,0)
    self.write("GAME OVER", align="center", font=("Arial", 12, "normal"))