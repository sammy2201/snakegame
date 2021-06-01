from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.penup()
        self.goto(x=0, y=260)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Score:{self.score}", align='center', font=('arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()



    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("game over", align='center', font=('arial', 24, 'normal'))
