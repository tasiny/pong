from turtle import Turtle


class Midline:
    def __init__(self):
        self.mid_line = Turtle()
        self.mid_line.pensize(5)
        self.mid_line.speed("fastest")
        self.mid_line.hideturtle()
        self.mid_line.penup()
        self.mid_line.color("white")
        self.mid_line.goto(0, 300)
        self.mid_line.right(90)
        for _ in range(10):
            self.mid_line.pendown()
            self.mid_line.forward(30)
            self.mid_line.penup()
            self.mid_line.forward(30)
