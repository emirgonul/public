from turtle import Screen, Turtle

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    #display scoreboard on initialization
    self.update_scoreboard()
    

  def update_scoreboard(self):
    #clear screen as the score updates
    self.clear()
    #left side score
    self.goto(-100, 200)
    self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
     #right side score
    self.goto(100, 200)
    self.write(self.r_score, align="center", font=("Courier", 50, "normal"))
    
  def l_point(self):
    self.l_score += 1
    self.update_scoreboard()

  def r_point(self):
    self.r_score += 1
    self.update_scoreboard()
