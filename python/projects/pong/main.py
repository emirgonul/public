from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Emir Pong")
#turn off animation
screen.tracer(0)

scoreboard = Scoreboard()
#initiate right & left paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
#paddle movement
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()


game_is_on = True
while game_is_on:
  #sleep method to slow screen refresh time, setting ball speed
  time.sleep(ball.move_speed)
  #update screen to reflect paddle movements
  screen.update()
  #move ball
  ball.move()
  #detect collision with wall and bounce
  if ball.ycor() > 280 or ball.ycor() < -280:
    #bounce when the ball hits the wall
    ball.bounce_y()
  #detect collision with right paddle
    #use .distance method to detect when ball is near the paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
      
  #detect when right paddle misses
  if ball.xcor() > 380:
    ball.reset_position()
    #update score
    scoreboard.l_point()

  #detect when left paddle misses
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()

screen.exitonclick()