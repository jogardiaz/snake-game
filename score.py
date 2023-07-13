from turtle import Turtle

ALIGN="center"
FONT = ('cOURIER', 15, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open('data.txt', mode='r') as data:
            self.high_score = data.read()
        self.score = -1
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.new_score()

    def new_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}   Higher Score: {self.high_score}", False, align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            with open('data.txt', mode='w') as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = -1
        self.new_score()

