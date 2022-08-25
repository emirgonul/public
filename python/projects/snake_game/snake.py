from turtle import Turtle, Screen

#list of tuples to create starting positions
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
#constant to set movement distance
MOVE_DISTANCE = 20
#constants to setup movement rules
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()
class Snake:

  def __init__(self):
    #list to keep segments
    self.segments = []
    #initialize snake object
    self.create_snake()
    #attribute to set head of snake to the first created segment
    self.head = self.segments[0]

  def create_snake(self):
    #create new turtle/snake object
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  def add_segment(self, position):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    #assign position to segment
    new_segment.goto(position)
    #add segment to the list of segments
    self.segments.append(new_segment)
    
  def extend(self):
    #add a new segment to the snake from the last spot in the list
    self.add_segment(self.segments[-1].position())

    
  def move(self):
    #go through segments list in reverse order to set follow logic
    for seg_num in range(len(self.segments) - 1 , 0 , -1 ):
      #set x,y coordinates to from previous segment(second to last segment)
      new_x = self.segments[seg_num -1].xcor()
      new_y = self.segments[seg_num -1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    #check to disable opposite movements of the head
    #if the current heading is pointed down, it cant move backwards
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    #it already going up, it's not allowed to go up
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
    
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
    
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)

