import turtle as trtl

# create spider body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

# create spider head
spider.goto(0, -30)
spider.circle(5)

# configure spider legs
num_legs = 8
leg_length = 50 # reduce length
angle = 360/num_legs - 25 # reduce angle
spider.pensize(5)

# draw curved legs
leg = 0
radius = 60
while leg < num_legs:
  spider.goto(0,20)
  if leg < 4:
    spider.setheading(angle*leg + 125)
    spider.pendown()
    spider.circle(radius, 120)
    spider.penup()
  else:
    spider.setheading(angle*leg + 90)
    spider.pendown()
    spider.circle(radius, -120)
    spider.penup()

  leg = leg + 1

# draw eyes
spider.pensize(5)
spider.color("mediumpurple")
spider.penup()
spider.goto(-5, -35)
spider.pendown()
spider.circle(5)
spider.penup()
spider.goto(5, -35)
spider.pendown()
spider.circle(5)

spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()