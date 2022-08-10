from turtle import Turtle
STARTING_POSITIONS = [(-360, 0), (360, 0)]
PADDLE_DISTANCE = 60


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.player_list = []
        self.create_paddles()
        self.player_1 = self.player_list[0]
        self.player_2 = self.player_list[1]

    def create_paddles(self):
        for position in STARTING_POSITIONS:
            self.player = Turtle()
            self.player_list.append(self.player)
            self.player.penup()
            self.player.color("white")
            self.player.shape("square")
            self.player.shapesize(stretch_wid=5.0, stretch_len=1)
            self.player.showturtle()
            self.player.goto(position)

    def player1_up(self):
        new_y = self.player_1.ycor() + 20
        self.player_1.goto(self.player_1.xcor(), new_y)

    def player1_down(self):
        new_y = self.player_1.ycor() - 20
        self.player_1.goto(self.player_1.xcor(), new_y)

    def player2_up(self):
        new_y = self.player_2.ycor() - 20
        self.player_2.goto(self.player_2.xcor(), new_y)

    def player2_down(self):
        new_y = self.player_2.ycor() + 20
        self.player_2.goto(self.player_2.xcor(), new_y)

