from turtle import Turtle
from pong_screen import PongScreen, LINE_COLOR, HALF_WIDTH, HALF_HEIGHT

MARGIN_H = 20
MARGIN_TOP = 56
MARGIN_BOTTOM = 72
LEFT_X = 12 + MARGIN_H - HALF_WIDTH
RIGHT_X = HALF_WIDTH - 20 - MARGIN_H
MOVE_STEP = 3


class Paddle(Turtle):
    def __init__(self, pong: PongScreen, player: str):
        super().__init__(shape="square")
        self.color(LINE_COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.pong = pong
        self.velocity = 0
        if player and (player.lower() == "left" or player.lower() == "l"):
            self.setx(LEFT_X)
        elif player and (player.lower() == "right" or player.lower() == "r"):
            self.setx(RIGHT_X)
        else:
            raise ValueError("Value of player should be 'left' or 'right'")

    def move(self):
        if self.velocity == 0:
            return
        moving_up = self.velocity > 0
        moving_down = self.velocity < 0
        pos_y = self.ycor()
        if (moving_up and pos_y < HALF_HEIGHT - MARGIN_TOP) or (moving_down and pos_y > MARGIN_TOP - HALF_HEIGHT):
            self.sety(pos_y + self.velocity)

    def down(self):
        self.velocity = -MOVE_STEP * self.pong.game_speed

    def up(self):
        self.velocity = MOVE_STEP * self.pong.game_speed

    def stop(self):
        self.velocity = 0
