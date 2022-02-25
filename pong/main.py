from turtle import Screen
from paddle import Paddle
from ball import Ball, BALL_POSITION
from scoreboard import Scoreboard
import time

POS_R_X = 350
POS_L_X = -350
POSITION_R = (POS_R_X, 0)
POSITION_L = (POS_L_X, 0)


score_l = 0
score_r = 0

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")

l_paddle = Paddle(POSITION_L)
r_paddle = Paddle(POSITION_R)
ball = Ball(BALL_POSITION)
scoreboard = Scoreboard()

screen.listen()
# screen.onkey(fun=l_paddle.up, key="w")
# screen.onkey(fun=l_paddle.down, key="s")
# screen.onkey(fun=r_paddle.up, key="Up")
# screen.onkey(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.time_out)

    # detect collision with wall
    if (ball.ycor() <= -290) or (ball.ycor() >= 290):
        ball.bounce_wall()

    # Detect collision with paddles
    if ((ball.xcor() >= POS_R_X - 10) and (ball.distance(r_paddle) < 50)) or (
            (ball.xcor() <= POS_L_X + 10) and (ball.distance(l_paddle) < 50)):
        ball.bounce_paddle()

    # Detect when the Ball goes out of Bounds
    if ball.xcor() > POS_R_X + 10:
        scoreboard.increase_score_r()
        ball.start_position()
    elif ball.xcor() < POS_L_X - 10:
        scoreboard.increase_score_l()
        ball.start_position()





screen.exitonclick()