from screen_setup import Midline
from turtle import Screen
from paddles import Paddle
from pong_ball import PongBall
import time
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.tracer(0)
my_screen.bgcolor("black")
mid_line = Midline()
paddles = Paddle()
my_ball = PongBall()
player1_score = ScoreBoard(-150, 220)
player2_score = ScoreBoard(150, 220)
my_screen.listen()
game_on = True
my_screen.onkey(fun=paddles.player1_up, key="w")
my_screen.onkey(fun=paddles.player1_down, key="s")
my_screen.onkey(fun=paddles.player2_up, key="Down")
my_screen.onkey(fun=paddles.player2_down, key="Up")

while game_on:
    time.sleep(0.05)
    my_screen.update()
    my_ball.forward(10)

#TOP AND BOTTOM WALL COLLISION DETECTION
    if my_ball.ycor() >= 290 or my_ball.ycor() <= -290:
        my_ball.setheading(360 - int(my_ball.heading()))

#PLAYER 2 COLLISION CONDITIONALS

    elif my_ball.distance(paddles.player_2) < 20:
        my_ball.setheading(360 - int(my_ball.heading()) + 180)
        my_ball.forward(10)
    elif my_ball.distance(paddles.player_2.xcor(), paddles.player_2.ycor() + 20) < 20:
        my_ball.setheading(360 - int(my_ball.heading()) + 140)
        my_ball.forward(10)
    elif my_ball.distance(paddles.player_2.xcor(), paddles.player_2.ycor() + 40) < 20:
        my_ball.setheading(360 - int(my_ball.heading()) + 160)
        my_ball.forward(10)
    elif my_ball.distance(paddles.player_2.xcor(), paddles.player_2.ycor() - 20) < 20:
        my_ball.setheading(360 - int(my_ball.heading()) + 200)
        my_ball.forward(10)
    elif my_ball.distance(paddles.player_2.xcor(), paddles.player_2.ycor() - 40) < 20:
        my_ball.setheading(360 - int(my_ball.heading()) + 220)
        my_ball.forward(10)

#PLAYER 1 COLLISION CONDITIONALS

    elif my_ball.distance(paddles.player_1) < 20:
        my_ball.setheading(360 - int(my_ball.heading()) + 180)
        my_ball.forward(10)
    elif my_ball.distance(paddles.player_1.xcor(), paddles.player_1.ycor() + 20) < 20:
        my_ball.setheading(360 - int(my_ball.heading()) + 200)
        my_ball.forward(10)
    elif my_ball.distance(paddles.player_1.xcor(), paddles.player_1.ycor() + 40) < 20:
        my_ball.setheading(360 - int(my_ball.heading()) + 220)
        my_ball.forward(10)
    elif my_ball.distance(paddles.player_1.xcor(), paddles.player_1.ycor() - 20) < 20:
        my_ball.setheading(360 - int(my_ball.heading()) + 160)
        my_ball.forward(10)
    elif my_ball.distance(paddles.player_1.xcor(), paddles.player_1.ycor() - 40) < 20:
        my_ball.setheading(360 - int(my_ball.heading()) + 140)
        my_ball.forward(10)

#OUT OF BOUNDS CONDITIONAL
    elif my_ball.xcor() >= 400:
        my_ball.reset_ball()
        player1_score.clear()
        player1_score.increase_score()
    elif my_ball.xcor() <= -400:
        my_ball.reset_ball()
        player2_score.clear()
        player2_score.increase_score()

my_screen.exitonclick()
