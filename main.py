from pong_screen import PongScreen
from paddle import Paddle
from ball import Ball
import time

pong = PongScreen()
screen = pong.screen
left_paddle = Paddle(pong, "L")
right_paddle = Paddle(pong, "R")
ball = Ball(pong)

screen.listen()
screen.onkey(pong.exit_game, "x")
screen.onkey(pong.increase_speed, "+")
screen.onkey(pong.decrease_speed, "-")

screen.onkeypress(left_paddle.up, "w")
screen.onkeyrelease(left_paddle.stop, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeyrelease(left_paddle.stop, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeyrelease(right_paddle.stop, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeyrelease(right_paddle.stop, "Down")

while pong.is_game_on:
    ball.move()
    left_paddle.move()
    right_paddle.move()
    ball.check_collision(left_paddle, right_paddle)
    if ball.beyond_right():
        ball.refresh()
        # TODO: Add score to left player
    elif ball.beyond_left():
        ball.refresh()
        # TODO: Add score to right player
    screen.update()
    time.sleep(0.01)

if not pong.player_exiting:
    screen.exitonclick()
