from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
    #inherit from Turtle class
      super().__init__()
      #set shape, color, size from 20x20
      self.shape("square")
      self.color("white")
      self.shapesize(stretch_wid=5, stretch_len=1)
      self.penup()
      self.goto(position)

    #paddle movement
    #movement methods
    def go_up(self):
      #only y position changes for up
      new_y = self.ycor() + 20
      self.goto(self.xcor(), new_y)

    def go_down(self):
      #only y position changes for up
      new_y = self.ycor() - 20
      self.goto(self.xcor(), new_y)
