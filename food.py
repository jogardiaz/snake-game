from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color('darkgreen')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)
        direction = random.randrange(0, 360, 90)
        self.setheading(direction)