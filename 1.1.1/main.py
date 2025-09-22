import turtle as trtl

painter = trtl.Turtle()

painter.turtlesize(2)
painter.pensize(2)
painter.forward(100)
painter.right(90)
painter.circle(100)

painter.teleport(2)
painter.circle(-100)

painter.teleport(50)

wn = trtl.Screen()
wn.mainloop()