from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

l_paddle_position = (-350, 0)
r_paddle_position = (350, 0)
l_scoreboard_pos = (-200, 280)
r_scoreboard_pos = (200, 280)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

l_paddle = Paddle(l_paddle_position)
r_paddle = Paddle(r_paddle_position)
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

while True:

    print(ball.move_speed)
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()







screen.exitonclick()