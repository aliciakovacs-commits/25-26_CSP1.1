import turtle as trtl

painter = trtl.Turtle()

painter.turtlesize(2)
painter.pensize(2)
painter.forward(100)
painter.right(90)
painter.circle(100)

painter.teleport(2)
painter.circle(-100)

painter.teleport(-70)
painter.circle(-30)

painter.teleport(170)
painter.circle(30)

painter.teleport(300)
painter.forward(-162)

painter.forward(162)
painter.teleport(-197)

painter.forward(-163)

painter.forward(163)

painter.teleport(-250)
painter.circle(300)

wn = trtl.Screen()
wn.mainloop()