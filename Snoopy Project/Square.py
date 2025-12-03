import turtle as trtl

ex = trtl.Turtle()
ex.speed(0)
length = 200

#Makes a square
for sides in range(4):
    ex.forward(length)
    ex.right(90)

wn = trtl.Screen()
wn.mainloop()