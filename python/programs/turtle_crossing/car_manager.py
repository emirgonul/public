from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#create car behavior
class CarManager:
  
  def __init__(self):
    #create all cars and store in list
    self.all_cars = []
    self.car_speed = STARTING_MOVE_DISTANCE

  def create_car(self):
    #reduce number of cars to 1 in 6
    random_chance = random.randint(1,6)
    if random_chance == 1:
      new_car = Turtle("square")
      new_car.shapesize(stretch_wid=1, stretch_len=2)
      new_car.penup()
      #create random car somewhere in the y axis
      new_car.color(random.choice(COLORS))
      random_y = random.randint(-250, 250)
      new_car.goto(300, random_y)
      #add new car to cars list
      self.all_cars.append(new_car)

  #move all of the cars by 5 paces
  def move_cars(self):
    for car in self.all_cars:
      car.backward(self.car_speed)

  #increase speed when car reaches finish line
  def level_up(self):
    self.car_speed += MOVE_INCREMENT
    