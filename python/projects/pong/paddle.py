from turtle import Screen, Turtle

#inherit from Turtle class
class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
  #set shape, color, size from 20x20
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    #start position
    self.goto(position)
    
  #movement methods
  def go_up(self):
    #only y position changes for up
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

  def go_down(self):
    #only y position changes for up
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)
  