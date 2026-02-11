from turtle import Turtle, Screen

s = Screen()
s.bgcolor("black")
s.screensize(600, 400)

l = []
for i in range(3):
    t = Turtle("square")
    t.color("white")
    t.shapesize(0.5, 0.5)
    t.penup()
    t.goto(-20*i, 0)   # start positions
    l.append(t)

for i in range(100):

    # move body from last to first
    for j in range(len(l)-1, 0, -1):
        x = l[j-1].xcor()
        y = l[j-1].ycor()
        l[j].goto(x, y)

    # move head forward
    l[0].forward(10)

s.exitonclick()
