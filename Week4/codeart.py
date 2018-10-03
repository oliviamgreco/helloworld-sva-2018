import turtle

t = turtle.Turtle()

t.color('black')
t.pensize(10)

side=600
t.penup()
t.goto(-200,-200) #makes it starts from bottom right of the screen
t.pendown()

#Start Spiral
for i in range (1,100):
  t.forward(side)
  t.left(90)
  side=side-20
