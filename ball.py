import random
from turtle import Turtle
from pong_screen import PongScreen, LINE_COLOR, HALF_WIDTH, HALF_HEIGHT

MARGIN_TOP = 12
MARGIN_BOTTOM = 18


class Ball(Turtle):
    def __init__(self, pong: PongScreen):
        super().__init__(shape="square")
        self.color(LINE_COLOR)
        self.penup()
        self.direction = get_rand_direction()
        self.pong = pong

    def move(self):
        if self.is_on_top() or self.is_on_bottom():
            dir_x = self.direction[0]
            dir_y = -self.direction[1]
            self.direction = (dir_x, dir_y)
        x = self.xcor() + (self.direction[0] * self.pong.game_speed)
        y = self.ycor() + (self.direction[1] * self.pong.game_speed)
        self.goto(x, y)

    def is_on_left_bound(self):
        is_going_left = self.direction[0] < 0
        return is_going_left and self.xcor() <= -HALF_WIDTH

    def is_on_right_bound(self):
        is_going_right = self.direction[0] > 0
        return is_going_right and self.xcor() >= HALF_WIDTH

    def is_on_top(self):
        is_going_up = self.direction[1] > 0
        return is_going_up and self.ycor() >= HALF_HEIGHT - MARGIN_TOP

    def is_on_bottom(self):
        is_going_down = self.direction[1] < 0
        return is_going_down and self.ycor() <= MARGIN_BOTTOM - HALF_HEIGHT

    def refresh(self):
        self.direction = get_rand_direction()
        self.goto(0, 0)


def get_rand_direction():
    x = 0
    while x == 0:
        x = random.randint(-2, 2)
    y = 0
    speed_y = 3 - abs(x)  # to limit speed of ball
    while y == 0:
        y = random.randint(-1, 1)
    result = (x, y * speed_y)
    return result
