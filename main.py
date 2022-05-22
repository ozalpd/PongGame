from pong_screen import PongScreen
from paddle import Paddle
import time

pong = PongScreen()
screen = pong.screen
left_paddle = Paddle(pong, "L")
right_paddle = Paddle(pong, "R")

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
    left_paddle.move()
    right_paddle.move()
    screen.update()
    time.sleep(0.01)

if not pong.player_exiting:
    screen.exitonclick()
