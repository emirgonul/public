from turtle import Turtle
import random

#render itself as a block
#snake touches food, food moves to random location

class Food(Turtle):
  #food class to inherit from turtle(snake class) to use it's methods/attributes
  def __init__(self):
    super().__init__()
    #method from turtle class
    self.shape("circle")
    self.penup()
    #create food object
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.color("blue")
    self.speed("fastest")
    #food to appear when initialized
    self.refresh()
    

  #food to refresh at a random location
  def refresh(self):
    #food coordinates randomly generated
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    #move to random location on the 300x300 canvas
    self.goto(random_x, random_y)
    