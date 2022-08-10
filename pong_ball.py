from turtle import Turtle
import random
HEADING = [x for x in range(0, 45)] + [x for x in range(315, 360)] + [x for x in range(135, 180)] + \
          [x for x in range(180, 225)]
Y_ALIGNMENT = [x for x in range(-260, 260)]


class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(3)
        self.color("white")
        self.shape("circle")
        self.goto(0, random.choice(Y_ALIGNMENT))
        self.setheading(random.choice(HEADING))

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def reset_ball(self):
        self.goto(0, 0)
        self.setheading(random.choice(HEADING))
