#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
#Create spider body
body = trtl.Turtle()
body.pensize(40)
body.circle(20)
#Configure spider legs
num_of_leg = 8
length = 70
direction = 360 / num_of_leg
body.pensize(5)
sub_leg = 0
radius = 60

#Draw legs
while (sub_leg < num_of_leg):
  body.goto(0,20)
  if sub_leg < 4:
      body.setheading(direction*sub_leg + 125)
      body.pendown()
      body.circle(radius, 120)
      body.penup()
  else:
      body.setheading(direction*sub_leg + 90)
      body.pendown()
      body.circle(radius, -120)
      body.penup()

    leg

print("direction=", direction)
("direction*sub_leg=", direction*sub_leg)

#Create spider eyes
body = trtl.Turtle()
body.color("white")
body.pensize(5)
body.circle(2)

wn = trtl.Screen()
wn.mainloop()