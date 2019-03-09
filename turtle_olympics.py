from turtle import *

positions = [
  [0,0, 'blue'],
  [-120, 0, 'purple'],
  [60, 60, 'red'],
  [-60, 60, 'yellow'],
  [-180, 60, 'green'],
]
myTurtle = Turtle(shape="turtle")
bgcolor("black")

for position in positions:
  myTurtle.pensize(5)
  myTurtle.color(position[2])
  myTurtle.penup()
  myTurtle.setposition(position[0], position[1])
  myTurtle.pendown()
  myTurtle.circle(50)



 
mainloop()