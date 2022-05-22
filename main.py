from pong_screen import PongScreen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

pong = PongScreen()
screen = pong.screen
left_paddle = Paddle(pong, "L")
left_scoreboard = ScoreBoard(-80, 260)
right_paddle = Paddle(pong, "R")
right_scoreboard = ScoreBoard(200, 260)
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
        if ball.is_going_right():
            ball.bounce(horizontally=True)  # start against to one had the score
        left_scoreboard.increase_score()
    elif ball.beyond_left():
        ball.refresh()
        if ball.is_going_left():
            ball.bounce(horizontally=True)  # start against to one had the score
        right_scoreboard.increase_score()
    screen.update()
    time.sleep(ball.sleep_time)

if not pong.player_exiting:
    screen.exitonclick()
