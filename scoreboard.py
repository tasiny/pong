from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x, y)
        self.write(f"{self.score}", font=("Comic Sans MS", 40, "bold"))

    def increase_score(self):
        self.score += 1
        self.write(f"{self.score}", font=("Comic Sans MS", 40, "bold"))
