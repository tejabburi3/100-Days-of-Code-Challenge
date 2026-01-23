from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 10

class snake_move:
    def __init__(self):
        self.list_turtle = []
        self.create_snake()
        self.head = self.list_turtle[0]

    def create_snake(self):
        for _ in range(3):
            self.add_segment()

    def add_segment(self):
        t = Turtle("square")
        t.shapesize(0.5, 0.5)
        t.color("white")
        t.penup()
        self.list_turtle.append(t)

    def add_segment_at(self, position):
        t = Turtle("square")
        t.shapesize(0.5, 0.5)
        t.color("white")
        t.penup()
        t.goto(position)
        self.list_turtle.append(t)

    def extend(self):
        self.add_segment_at(self.list_turtle[-1].position())

    def move(self):
        for i in range(len(self.list_turtle) - 1, 0, -1):
            self.list_turtle[i].goto(self.list_turtle[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
