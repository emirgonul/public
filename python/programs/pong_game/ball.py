from turtle import Turtle

#create the ball and make it move
class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    #everytime x,y move, increase by 10
    self.x_move = 10
    self.y_move = 10
    #ball speed level
    self.move_speed = 0.1
    
#move ball by updating x,y coordinates
  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def bounce_y(self):
    #reverse direction on bounce by multiplying by -1
    self.y_move *= -1

  def bounce_x(self):
    #reverse direction on bounce by multiplying by -1
    self.x_move *= -1
    #each time ball bounces,ball speed increases
    self.move_speed *= 0.9

  #reset position when ball is missed and reverse direction
  def reset_position(self):
    self.goto(0,0)
    #set speed to game beginnning
    self.move_speed = 0.1
    self.bounce_x()