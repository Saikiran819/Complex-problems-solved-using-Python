import turtle

f = turtle.Turtle()
f.color("red", "yellow")
f.speed(10)
f.begin_fill()
for x in range(100):
    f.forward(300)
    f.left(168.5)
f.end_fill()
turtle.done()