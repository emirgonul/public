from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
#set screen diameter
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
#set screen to 0, blank
screen.tracer(0)

#object from snake class
snake = Snake()
#food object
food = Food()
#scoreboard object
scoreboard = Scoreboard()

#listen to key strokes
screen.listen()

up =screen.onkey(snake.up, "Up")
down = screen.onkey(snake.down, "Down")
left = screen.onkey(snake.left, "Left")
right = screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
  #update screen
  screen.update()
  #delay between forward movements
  time.sleep(0.5)
  #call method from snake class
  snake.move()
  #detect collision(eat) with food & refresh after collision
  if snake.head.distance(food) < 15:
    #new food moves to random spot
    food.refresh()
    #snake eats the food & increases score
    snake.extend()
    scoreboard.increase_score()

  #detect collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False
    scoreboard.game_over()

  #detect when snake collides with own body
  #loop through all the segments except the first one using slicing
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over

#waits for user to exit
screen.exitonclick()