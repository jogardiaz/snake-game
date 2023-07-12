from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.x = 0
        self.segments = []
        self.initializa()
        self.head = self.segments[0]

    def initializa(self):
        for i in range(3):
            self.x -= 20
            self.add_segments((self.x, 0))

    def add_segments(self, position):
        turtle = Turtle('square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)

        self.segments.append(turtle)

    def extend(self):
        self.add_segments(self.segments[-1].position())


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            nex_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(nex_x, new_y)
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