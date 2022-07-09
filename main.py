from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.tracer(0)
my_screen.setup(width=800, height=600)
my_screen.title('Pong game')
my_screen.bgcolor('black')

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
score_board = Scoreboard()
ball = Ball()

my_screen.listen()
my_screen.onkeypress(r_paddle.up, 'Up')
my_screen.onkeypress(r_paddle.down, 'Down')
my_screen.onkeypress(l_paddle.up, 'w')
my_screen.onkeypress(l_paddle.down, 's')

is_movement = True
while is_movement:
    time.sleep(ball.ball_speed)
    my_screen.update()
    ball.move()

    # Detect collision with the wall and bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.y_bounce()
    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Detect when the r_paddle misses
    if ball.xcor() > 380:
        ball.reset()
        score_board.l_point()

    # Detect when the l_paddle misses
    if ball.xcor() < -380:
        ball.reset()
        score_board.r_point()

my_screen.exitonclick()
