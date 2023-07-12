from turtle import Turtle

ALIGN="center"
FONT = ('cOURIER', 15, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.new_score()

    def new_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGN, font=FONT)